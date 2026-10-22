'use strict';
const fs=require('node:fs');
const {resolve}=require('node:path');
function parseUrl(value,field,issues){
 if(typeof value!=='string'||!value.trim()){issues.push({severity:'error',code:'MISSING_URL',field});return null;}
 try{
  const u=new URL(value);
  if(!['http:','https:'].includes(u.protocol)){issues.push({severity:'error',code:'INVALID_SCHEME',field});return null;}
  if(u.username||u.password){issues.push({severity:'error',code:'URL_WITH_CREDENTIALS',field});return null;}
  return u;
 }catch{issues.push({severity:'error',code:'MALFORMED_URL',field});return null;}
}
function normalize(u){return u.origin+(u.pathname.replace(/\/+$/,'')||'/')+u.search;}
function check(input){
 const issues=[];
 const site=parseUrl(input.siteUrl,'siteUrl',issues);
 const redirect=parseUrl(input.redirectTo,'redirectTo',issues);
 const list=Array.isArray(input.redirectAllowList)?input.redirectAllowList:[];
 if(!Array.isArray(input.redirectAllowList))issues.push({severity:'error',code:'ALLOWLIST_TYPE',field:'redirectAllowList'});
 const exact=[];let hasPatterns=false;
 list.forEach((entry,i)=>{
  if(typeof entry!=='string'||!entry.trim()){issues.push({severity:'warning',code:'EMPTY_ENTRY',field:'redirectAllowList['+i+']'});return;}
  if(/[!*?]/.test(entry)){hasPatterns=true;issues.push({severity:'info',code:'PATTERN_NOT_EVALUATED',field:'redirectAllowList['+i+']'});return;}
  const u=parseUrl(entry,'redirectAllowList['+i+']',issues);if(u)exact.push(normalize(u));
 });
 for(const [field,u] of [['siteUrl',site],['redirectTo',redirect]]){
  if(u&&u.protocol!=='https:'&&!['localhost','127.0.0.1','[::1]'].includes(u.hostname)){
   issues.push({severity:'warning',code:'NON_HTTPS_PRODUCTION',field});
  }
 }
 if(redirect){
  const matched=[...(site?[normalize(site)]:[]),...exact].includes(normalize(redirect));
  issues.push({severity:matched?'info':'warning',code:matched?'EXACT_URL_MATCH':hasPatterns?'PATTERN_REQUIRES_MANUAL_CHECK':'NO_EXACT_REDIRECT_MATCH',field:'redirectTo'});
  if(site&&site.origin!==redirect.origin){issues.push({severity:'info',code:'CROSS_ORIGIN_REDIRECT',field:'redirectTo'});}
 }
 issues.push({severity:'info',code:'NOT_LIVE_AUTH_TEST',field:'runtime'});
 return {issues,counts:{errors:issues.filter(i=>i.severity==='error').length,warnings:issues.filter(i=>i.severity==='warning').length}};
}
if(require.main===module){
 try{
  const f=process.argv[2]||resolve(__dirname,'example-config.json');
  const result=check(JSON.parse(fs.readFileSync(f,'utf8')));
  process.stdout.write(JSON.stringify(result,null,2)+'\n');
  if(result.counts.errors)process.exitCode=2;
 }catch(e){process.stderr.write('Diagnostic input error: '+e.message+'\n');process.exitCode=2;}
}
module.exports={check};
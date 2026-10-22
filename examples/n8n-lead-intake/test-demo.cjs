const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict');
const w=JSON.parse(fs.readFileSync(__dirname+'/workflow.json','utf8'));
assert.equal(w.nodes.length,4);
assert.equal(w.active,false);
assert.equal(w.nodes.filter(n=>n.type==='n8n-nodes-base.code').length,3);
const codeNode=(name,items)=>{
  const n=w.nodes.find(x=>x.name===name);
  const result=vm.runInNewContext('(function(){'+n.parameters.jsCode+'\n})()',{$input:{all:()=>items}});
  assert.ok(Array.isArray(result));return result;
};
const created=codeNode('Generate Synthetic Form Events',[{json:{}}]);
const normalized=codeNode('Validate and Deduplicate',created);
const preview=codeNode('Preview CRM Actions (No API Calls)',normalized);
assert.deepEqual([...normalized.map(x=>x.json.status)],['ready','invalid','duplicate','ready']);
assert.deepEqual([...preview.map(x=>x.json.action)],['SIMULATED_CRM_CREATE','SKIPPED','SKIPPED','SIMULATED_CRM_CREATE']);
assert.equal(normalized[0].json.name,'Alice');
assert.equal(normalized[1].json.email,'bad-address');
assert.equal(preview.every(x=>x.json.note.length>0),true);
console.log('PASS: 4 demo items, validation, dedupe, and dry-run CRM mapping; no external API calls.');
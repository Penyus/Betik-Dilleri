y=prompt('isim giriniz:gulsenem?hurlika?');                        // Mehmet Gediklioğlu
if(y=='gulsenem'){
   for(let i=0; i<y.length;i++){
      alert(y[i]);}}
   else if(y=='hurlika'){
   for(let i=y.length -1;i>0; i--){
   
   alert(y[i]);}}
else{
   alert('yanlış isim girildi');}
---------------------------------------
a=['hurlika','gonca','nasiba','gulsenem']
for (let i=0; i<a.length; i++){
console.log(a[i]);
alert(i);
}
------------------------------------
a=prompt('isminizi yazınız'); 
alert(a);
------------------------------------
for(let i=0; i<a.length; i++){
console.log veya alert (a[i])
-----------------------------------
ör:
x=prompt('isim yaz');
if(x=='gulsenem'){
.....
}
else if(x=='hurlika'){
.....
}
else{
alert('yanlış isim girildi')}

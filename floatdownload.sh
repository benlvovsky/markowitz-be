#!/bin/bash

rm -rf floatdatadownload
mkdir -p floatdatadownload

#wget -P floatdatadownload "http://float.com.au/download/2008.zip"
#wget -P floatdatadownload "http://float.com.au/download/2009.zip"
#wget -P floatdatadownload "http://float.com.au/download/2010.zip"
#wget -P floatdatadownload "http://float.com.au/download/2011.zip"
#wget -P floatdatadownload "http://float.com.au/download/2012.zip"
#wget -P floatdatadownload "http://float.com.au/download/2013.zip"
#wget -P floatdatadownload "http://float.com.au/download/2014.zip"
#wget -P floatdatadownload "http://float.com.au/download/2015.zip"
#wget -P floatdatadownload "http://float.com.au/download/2016.zip"
#wget -P floatdatadownload "http://float.com.au/download/2017.zip"
#wget -P floatdatadownload "http://float.com.au/download/2018.zip"

wget -O floatdatadownload/asx200.zip "http://float.com.au/download/asx200.zip?ticker=abp,abc,agl,alq,alu,awc,amc,amp,ann,anz,apa,apo,arb,aad,all,ahy,asx,alx,azj,asl,ast,api,ahg,aog,boq,bap,bpt,bga,bal,ben,bhp,bkl,bsl,bld,bxb,brg,bkw,bwp,ctx,car,cgf,chc,cqr,cnu,clw,cim,cwy,ccl,coh,cba,cpu,ctd,cgc,ccp,cmw,cwn,csl,csr,cyb,dxs,dhg,dmp,dow,dlx,ecx,ehe,evn,fxj,fph,fbu,flt,fmg,gud,gem,gxy,gty,gma,gmg,gpt,gnc,gxl,goz,gwa,hvn,hso,iel,ilu,ipl,igo,ifn,iag,iof,ivc,ifl,iph,ire,inm,jhx,jhg,jbh,a2m,llc,lnk,lyc,mfg,mgr,min,mms,mnd,mpl,mqg,mts,myo,myx,nab,nan,ncm,nec,nhf,nsr,nst,nuf,nvt,nws,nxt,oml,ora,ore,org,ori,osh,ozl,pdl,pgh,pls,pmv,ppt,pry,ptm,qan,qbe,qub,rea,rfg,rhc,rio,rmd,rrl,rsg,rwc,s32,sar,sbm,scg,scp,sda,sdf,sek,sfr,sgm,sgp,sgr,shl,sig,siq,skc,ski,sol,spk,srx,sto,sul,sun,svw,swm,sxl,syd,syr,tah,tcl,tgr,tls,tme,tne,tpm,twe,vcx,voc,vvr,wbc,web,wes,wfd,whc,wor,wow,wpl,wsa,wtc,xro"

cd floatdatadownload

unzip "*.zip"

cat ./*.txt > b.txt

#rm *.txt

"use strict";(self.webpackChunk=self.webpackChunk||[]).push([[96],{31622:function(ve,F,e){e.d(F,{Di:function(){return te},MB:function(){return ee},NS:function(){return g},V7:function(){return Y},cK:function(){return X},wO:function(){return l}});var q=e(17061),V=e.n(q),ae=e(17156),_=e.n(ae),K=e(12439),X=function(){var h=_()(V()().mark(function d(v){var i;return V()().wrap(function(t){for(;;)switch(t.prev=t.next){case 0:return t.prev=0,t.next=3,K.Z.post("/getinformation/submit_form",v);case 3:return i=t.sent,t.abrupt("return",i);case 7:throw t.prev=7,t.t0=t.catch(0),console.error("Failed to submit form:",t.t0),t.t0;case 11:case"end":return t.stop()}},d,null,[[0,7]])}));return function(v){return h.apply(this,arguments)}}(),G=function(d){try{var v=request.post("/getinformation/getPersonInfo",d);return v}catch(i){throw console.error("Failed to get person info:",i),i}},Y=function(d){try{var v=K.Z.post("/getinformation/getData1",d);return v}catch(i){throw console.error("Failed to get person info:",i),i}},l=function(d){try{var v=K.Z.post("/getinformation/getData2",d);return v}catch(i){throw console.error("Failed to get person info:",i),i}},ee=function(d){try{var v=K.Z.post("/getinformation/getData3",d);return v}catch(i){throw console.error("Failed to get person info:",i),i}},te=function(d){try{var v=K.Z.post("/getinformation/getData4",d);return v}catch(i){throw console.error("Failed to get person info:",i),i}},g=function(d){try{var v=K.Z.post("/getinformation/calculateInfo",d);return v}catch(i){throw console.error("Failed to get person info:",i),i}}},11149:function(ve,F,e){e.d(F,{Z:function(){return q}});var q="20250208"},3184:function(ve,F,e){e.d(F,{RZ:function(){return g},bv:function(){return K},pe:function(){return G},r$:function(){return X}});var q=e(861),V=e.n(q),ae=e(18698),_=e.n(ae);function K(d){var v=arguments.length>1&&arguments[1]!==void 0?arguments[1]:[],i=d.replace(/^```json\s*/,"").replace(/```$/,""),$;try{$=JSON.parse(i)}catch(t){return console.error("JSON \u89E3\u6790\u9519\u8BEF:",t),null}return v.length>0&&$&&_()($)==="object"?Object.keys($).filter(function(t){return!v.some(function(A){return t.includes(A)})}).reduce(function(t,A){return t[A]=$[A],t},{}):$}var X=function(v,i){var $=new TextEncoder().encode(i),t=new TextEncoder().encode(v),A=t.map(function(H,ne){return H^$[ne%$.length]});return btoa(String.fromCharCode.apply(String,V()(A)))},G=function(v,i){try{for(var $=v.replace(/-/g,"+").replace(/_/g,"/"),t=atob($),A=new Uint8Array(t.length),H=0;H<t.length;H++)A[H]=t.charCodeAt(H);for(var ne=new TextEncoder().encode(i),se=new Uint8Array(A.length),c=0;c<A.length;c++)se[c]=A[c]^ne[c%ne.length];return new TextDecoder().decode(se)}catch(re){return console.error("\u89E3\u5BC6\u5931\u8D25:",re),null}},Y="mysecretkey",l="HelloWorld",ee=X(l,Y),te=G(ee,Y);console.log("\u539F\u6587\u672C:",l),console.log("\u52A0\u5BC6\u540E:",ee),console.log("\u89E3\u5BC6\u540E:",te);var g=function(v){return v.replace(/(.{2})/g,"$1 ")},h={processJsonString:K,simpleEncryptDecrypt:X,decrypt:G,formatText:g}},2378:function(ve,F,e){e.d(F,{Z:function(){return se}});var q=e(67294),V=e(33862),ae=e(38545),_=e(87547),K=e(26058),X=e(71230),G=e(15746),Y=e(7549),l=e(39539),ee=e(74627),te=e(93578),g=e(57210),h=e.p+"static/logo.73bb9853.png",d=e(20829),v=e(31622),i=e(3184),$=e(11149),t=e(85893),A=K.Z.Header,H=[{key:"1",label:"Home",path:"/"},{key:"2",label:"Discussion",path:"/discussion"},{key:"3",label:"1 VS 1 Service",path:"/1vs1"}],ne=function(){var re=(0,te.s0)(),me=function(){(0,d.fA)().then(function(Q){console.log(Q,"result"),Q!=null&&Q.loggedIn?(0,v.NS)({user:localStorage.getItem("user")}).then(function(w){var de=w.data||"";console.log((0,i.r$)(de,$.Z)),re("/setting/".concat((0,i.r$)(w.data,$.Z))),console.log(w.data)}):re("/login")})},fe=function(){console.log("User logged out"),(0,d.kS)()},je=(0,t.jsxs)("div",{children:[(0,t.jsx)("p",{className:g.Z.cursor,onClick:me,children:"\u6211\u7684\u62A5\u544A"}),(0,t.jsx)("p",{className:g.Z.cursor,onClick:fe,children:"\u9000\u51FA"})]}),Ie=function(Q){var w=H.find(function(de){return de.key===Q.key});w&&re(w.path)};return(0,t.jsx)(A,{style:{display:"flex",alignItems:"center",padding:"0px"},children:(0,t.jsxs)(X.Z,{style:{width:"100%"},children:[(0,t.jsx)(G.Z,{span:3,children:"col-8"}),(0,t.jsxs)(G.Z,{style:{display:"flex"},span:18,children:[(0,t.jsx)("img",{src:h,alt:"Logo",className:g.Z.demologo}),(0,t.jsx)(Y.Z,{theme:"dark",mode:"horizontal",defaultSelectedKeys:["1"],onClick:Ie,items:H,style:{flex:1,minWidth:0,position:"relative",fontFamily:"bold"}})]}),(0,t.jsx)(G.Z,{span:3,children:(0,t.jsxs)("div",{className:g.Z.font,children:[(0,t.jsx)(l.Z,{defaultValue:"English",style:{width:100},options:[{value:"Malay",label:"Malay"},{value:"English",label:"English"},{value:"Hindi",label:"Hindi"}]}),(0,t.jsx)(V.Z,{className:g.Z.cursor}),(0,t.jsx)(ae.Z,{className:g.Z.cursor}),(0,t.jsx)(ee.Z,{placement:"bottom",content:je,trigger:"click",children:(0,t.jsx)(_.Z,{className:g.Z.cursor})})]})})]})})},se=ne},78859:function(ve,F,e){e.r(F),e.d(F,{default:function(){return rn}});var q=e(56690),V=e.n(q),ae=e(89728),_=e.n(ae),K=e(61655),X=e.n(K),G=e(26389),Y=e.n(G),l=e(67294),ee=e(2378),te=e(90814),g=e(93967),h=e.n(g),d=e(87462),v=e(74902),i=e(97685),$=e(71002),t=e(21770),A=e(80334),H=e(91),ne=e(50344),se=e(1413),c=e(4942),re=e(29372),me=e(15105),fe=l.forwardRef(function(a,n){var r=a.prefixCls,s=a.forceRender,u=a.className,N=a.style,p=a.children,y=a.isActive,j=a.role,b=a.classNames,R=a.styles,x=l.useState(y||s),C=(0,i.Z)(x,2),m=C[0],I=C[1];return l.useEffect(function(){(s||y)&&I(!0)},[s,y]),m?l.createElement("div",{ref:n,className:h()("".concat(r,"-content"),(0,c.Z)((0,c.Z)({},"".concat(r,"-content-active"),y),"".concat(r,"-content-inactive"),!y),u),style:N,role:j},l.createElement("div",{className:h()("".concat(r,"-content-box"),b==null?void 0:b.body),style:R==null?void 0:R.body},p)):null});fe.displayName="PanelContent";var je=fe,Ie=["showArrow","headerClass","isActive","onItemClick","forceRender","className","classNames","styles","prefixCls","collapsible","accordion","panelKey","extra","header","expandIcon","openMotion","destroyInactivePanel","children"],ie=l.forwardRef(function(a,n){var r=a.showArrow,s=r===void 0?!0:r,u=a.headerClass,N=a.isActive,p=a.onItemClick,y=a.forceRender,j=a.className,b=a.classNames,R=b===void 0?{}:b,x=a.styles,C=x===void 0?{}:x,m=a.prefixCls,I=a.collapsible,M=a.accordion,f=a.panelKey,E=a.extra,T=a.header,D=a.expandIcon,P=a.openMotion,U=a.destroyInactivePanel,S=a.children,W=(0,H.Z)(a,Ie),B=I==="disabled",L=E!=null&&typeof E!="boolean",J=(0,c.Z)((0,c.Z)((0,c.Z)({onClick:function(){p==null||p(f)},onKeyDown:function(ue){(ue.key==="Enter"||ue.keyCode===me.Z.ENTER||ue.which===me.Z.ENTER)&&(p==null||p(f))},role:M?"tab":"button"},"aria-expanded",N),"aria-disabled",B),"tabIndex",B?-1:0),Z=typeof D=="function"?D(a):l.createElement("i",{className:"arrow"}),z=Z&&l.createElement("div",(0,d.Z)({className:"".concat(m,"-expand-icon")},["header","icon"].includes(I)?J:{}),Z),oe=h()("".concat(m,"-item"),(0,c.Z)((0,c.Z)({},"".concat(m,"-item-active"),N),"".concat(m,"-item-disabled"),B),j),$e=h()(u,"".concat(m,"-header"),(0,c.Z)({},"".concat(m,"-collapsible-").concat(I),!!I),R.header),pe=(0,se.Z)({className:$e,style:C.header},["header","icon"].includes(I)?{}:J);return l.createElement("div",(0,d.Z)({},W,{ref:n,className:oe}),l.createElement("div",pe,s&&z,l.createElement("span",(0,d.Z)({className:"".concat(m,"-header-text")},I==="header"?J:{}),T),L&&l.createElement("div",{className:"".concat(m,"-extra")},E)),l.createElement(re.ZP,(0,d.Z)({visible:N,leavedClassName:"".concat(m,"-content-hidden")},P,{forceRender:y,removeOnLeave:U}),function(Ce,ue){var on=Ce.className,ln=Ce.style;return l.createElement(je,{ref:ue,prefixCls:m,className:on,classNames:R,style:ln,styles:C,isActive:N,forceRender:y,role:M?"tabpanel":void 0},S)}))}),Q=ie,w=["children","label","key","collapsible","onItemClick","destroyInactivePanel"],de=function(n,r){var s=r.prefixCls,u=r.accordion,N=r.collapsible,p=r.destroyInactivePanel,y=r.onItemClick,j=r.activeKey,b=r.openMotion,R=r.expandIcon;return n.map(function(x,C){var m=x.children,I=x.label,M=x.key,f=x.collapsible,E=x.onItemClick,T=x.destroyInactivePanel,D=(0,H.Z)(x,w),P=String(M!=null?M:C),U=f!=null?f:N,S=T!=null?T:p,W=function(J){U!=="disabled"&&(y(J),E==null||E(J))},B=!1;return u?B=j[0]===P:B=j.indexOf(P)>-1,l.createElement(Q,(0,d.Z)({},D,{prefixCls:s,key:P,panelKey:P,isActive:B,accordion:u,openMotion:b,expandIcon:R,header:I,collapsible:U,onItemClick:W,destroyInactivePanel:S}),m)})},be=function(n,r,s){if(!n)return null;var u=s.prefixCls,N=s.accordion,p=s.collapsible,y=s.destroyInactivePanel,j=s.onItemClick,b=s.activeKey,R=s.openMotion,x=s.expandIcon,C=n.key||String(r),m=n.props,I=m.header,M=m.headerClass,f=m.destroyInactivePanel,E=m.collapsible,T=m.onItemClick,D=!1;N?D=b[0]===C:D=b.indexOf(C)>-1;var P=E!=null?E:p,U=function(B){P!=="disabled"&&(j(B),T==null||T(B))},S={key:C,panelKey:C,header:I,headerClass:M,isActive:D,prefixCls:u,destroyInactivePanel:f!=null?f:y,openMotion:R,accordion:N,children:n.props.children,onItemClick:U,expandIcon:x,collapsible:P};return typeof n.type=="string"?n:(Object.keys(S).forEach(function(W){typeof S[W]=="undefined"&&delete S[W]}),l.cloneElement(n,S))};function Pe(a,n,r){return Array.isArray(a)?de(a,r):(0,ne.Z)(n).map(function(s,u){return be(s,u,r)})}var Ee=Pe,Se=e(64217);function Ne(a){var n=a;if(!Array.isArray(n)){var r=(0,$.Z)(n);n=r==="number"||r==="string"?[n]:[]}return n.map(function(s){return String(s)})}var ge=l.forwardRef(function(a,n){var r=a.prefixCls,s=r===void 0?"rc-collapse":r,u=a.destroyInactivePanel,N=u===void 0?!1:u,p=a.style,y=a.accordion,j=a.className,b=a.children,R=a.collapsible,x=a.openMotion,C=a.expandIcon,m=a.activeKey,I=a.defaultActiveKey,M=a.onChange,f=a.items,E=h()(s,j),T=(0,t.Z)([],{value:m,onChange:function(L){return M==null?void 0:M(L)},defaultValue:I,postState:Ne}),D=(0,i.Z)(T,2),P=D[0],U=D[1],S=function(L){return U(function(){if(y)return P[0]===L?[]:[L];var J=P.indexOf(L),Z=J>-1;return Z?P.filter(function(z){return z!==L}):[].concat((0,v.Z)(P),[L])})};(0,A.ZP)(!b,"[rc-collapse] `children` will be removed in next major version. Please use `items` instead.");var W=Ee(f,b,{prefixCls:s,accordion:y,openMotion:x,expandIcon:C,collapsible:R,destroyInactivePanel:N,onItemClick:S,activeKey:P});return l.createElement("div",(0,d.Z)({ref:n,className:E,style:p,role:y?"tablist":void 0},(0,Se.Z)(a,{aria:!0,data:!0})),W)}),ce=Object.assign(ge,{Panel:Q}),he=ce,le=ce.Panel,ye=e(98423),Me=e(33603),O=e(96159),Re=e(53124),Be=e(98675),Ke=l.forwardRef((a,n)=>{const{getPrefixCls:r}=l.useContext(Re.E_),{prefixCls:s,className:u,showArrow:N=!0}=a,p=r("collapse",s),y=h()({[`${p}-no-arrow`]:!N},u);return l.createElement(he.Panel,Object.assign({ref:n},a,{prefixCls:p,className:y}))}),k=e(11568),Ae=e(14747),Fe=e(33507),He=e(83559),Le=e(83262);const ze=a=>{const{componentCls:n,contentBg:r,padding:s,headerBg:u,headerPadding:N,collapseHeaderPaddingSM:p,collapseHeaderPaddingLG:y,collapsePanelBorderRadius:j,lineWidth:b,lineType:R,colorBorder:x,colorText:C,colorTextHeading:m,colorTextDisabled:I,fontSizeLG:M,lineHeight:f,lineHeightLG:E,marginSM:T,paddingSM:D,paddingLG:P,paddingXS:U,motionDurationSlow:S,fontSizeIcon:W,contentPadding:B,fontHeight:L,fontHeightLG:J}=a,Z=`${(0,k.bf)(b)} ${R} ${x}`;return{[n]:Object.assign(Object.assign({},(0,Ae.Wf)(a)),{backgroundColor:u,border:Z,borderRadius:j,"&-rtl":{direction:"rtl"},[`& > ${n}-item`]:{borderBottom:Z,"&:first-child":{[`
            &,
            & > ${n}-header`]:{borderRadius:`${(0,k.bf)(j)} ${(0,k.bf)(j)} 0 0`}},"&:last-child":{[`
            &,
            & > ${n}-header`]:{borderRadius:`0 0 ${(0,k.bf)(j)} ${(0,k.bf)(j)}`}},[`> ${n}-header`]:Object.assign(Object.assign({position:"relative",display:"flex",flexWrap:"nowrap",alignItems:"flex-start",padding:N,color:m,lineHeight:f,cursor:"pointer",transition:`all ${S}, visibility 0s`},(0,Ae.Qy)(a)),{[`> ${n}-header-text`]:{flex:"auto"},[`${n}-expand-icon`]:{height:L,display:"flex",alignItems:"center",paddingInlineEnd:T},[`${n}-arrow`]:Object.assign(Object.assign({},(0,Ae.Ro)()),{fontSize:W,transition:`transform ${S}`,svg:{transition:`transform ${S}`}}),[`${n}-header-text`]:{marginInlineEnd:"auto"}}),[`${n}-collapsible-header`]:{cursor:"default",[`${n}-header-text`]:{flex:"none",cursor:"pointer"}},[`${n}-collapsible-icon`]:{cursor:"unset",[`${n}-expand-icon`]:{cursor:"pointer"}}},[`${n}-content`]:{color:C,backgroundColor:r,borderTop:Z,[`& > ${n}-content-box`]:{padding:B},"&-hidden":{display:"none"}},"&-small":{[`> ${n}-item`]:{[`> ${n}-header`]:{padding:p,paddingInlineStart:U,[`> ${n}-expand-icon`]:{marginInlineStart:a.calc(D).sub(U).equal()}},[`> ${n}-content > ${n}-content-box`]:{padding:D}}},"&-large":{[`> ${n}-item`]:{fontSize:M,lineHeight:E,[`> ${n}-header`]:{padding:y,paddingInlineStart:s,[`> ${n}-expand-icon`]:{height:J,marginInlineStart:a.calc(P).sub(s).equal()}},[`> ${n}-content > ${n}-content-box`]:{padding:P}}},[`${n}-item:last-child`]:{borderBottom:0,[`> ${n}-content`]:{borderRadius:`0 0 ${(0,k.bf)(j)} ${(0,k.bf)(j)}`}},[`& ${n}-item-disabled > ${n}-header`]:{"\n          &,\n          & > .arrow\n        ":{color:I,cursor:"not-allowed"}},[`&${n}-icon-position-end`]:{[`& > ${n}-item`]:{[`> ${n}-header`]:{[`${n}-expand-icon`]:{order:1,paddingInlineEnd:0,paddingInlineStart:T}}}}})}},Ue=a=>{const{componentCls:n}=a,r=`> ${n}-item > ${n}-header ${n}-arrow`;return{[`${n}-rtl`]:{[r]:{transform:"rotate(180deg)"}}}},We=a=>{const{componentCls:n,headerBg:r,paddingXXS:s,colorBorder:u}=a;return{[`${n}-borderless`]:{backgroundColor:r,border:0,[`> ${n}-item`]:{borderBottom:`1px solid ${u}`},[`
        > ${n}-item:last-child,
        > ${n}-item:last-child ${n}-header
      `]:{borderRadius:0},[`> ${n}-item:last-child`]:{borderBottom:0},[`> ${n}-item > ${n}-content`]:{backgroundColor:"transparent",borderTop:0},[`> ${n}-item > ${n}-content > ${n}-content-box`]:{paddingTop:s}}}},Ge=a=>{const{componentCls:n,paddingSM:r}=a;return{[`${n}-ghost`]:{backgroundColor:"transparent",border:0,[`> ${n}-item`]:{borderBottom:0,[`> ${n}-content`]:{backgroundColor:"transparent",border:0,[`> ${n}-content-box`]:{paddingBlock:r}}}}}},Je=a=>({headerPadding:`${a.paddingSM}px ${a.padding}px`,headerBg:a.colorFillAlter,contentPadding:`${a.padding}px 16px`,contentBg:a.colorBgContainer});var Ve=(0,He.I$)("Collapse",a=>{const n=(0,Le.IX)(a,{collapseHeaderPaddingSM:`${(0,k.bf)(a.paddingXS)} ${(0,k.bf)(a.paddingSM)}`,collapseHeaderPaddingLG:`${(0,k.bf)(a.padding)} ${(0,k.bf)(a.paddingLG)}`,collapsePanelBorderRadius:a.borderRadiusLG});return[ze(n),We(n),Ge(n),Ue(n),(0,Fe.Z)(n)]},Je),Xe=Object.assign(l.forwardRef((a,n)=>{const{getPrefixCls:r,direction:s,collapse:u}=l.useContext(Re.E_),{prefixCls:N,className:p,rootClassName:y,style:j,bordered:b=!0,ghost:R,size:x,expandIconPosition:C="start",children:m,expandIcon:I}=a,M=(0,Be.Z)(Z=>{var z;return(z=x!=null?x:Z)!==null&&z!==void 0?z:"middle"}),f=r("collapse",N),E=r(),[T,D,P]=Ve(f),U=l.useMemo(()=>C==="left"?"start":C==="right"?"end":C,[C]),S=I!=null?I:u==null?void 0:u.expandIcon,W=l.useCallback(function(){let Z=arguments.length>0&&arguments[0]!==void 0?arguments[0]:{};const z=typeof S=="function"?S(Z):l.createElement(te.Z,{rotate:Z.isActive?s==="rtl"?-90:90:void 0,"aria-label":Z.isActive?"expanded":"collapsed"});return(0,O.Tm)(z,()=>{var oe;return{className:h()((oe=z==null?void 0:z.props)===null||oe===void 0?void 0:oe.className,`${f}-arrow`)}})},[S,f]),B=h()(`${f}-icon-position-${U}`,{[`${f}-borderless`]:!b,[`${f}-rtl`]:s==="rtl",[`${f}-ghost`]:!!R,[`${f}-${M}`]:M!=="middle"},u==null?void 0:u.className,p,y,D,P),L=Object.assign(Object.assign({},(0,Me.Z)(E)),{motionAppear:!1,leavedClassName:`${f}-content-hidden`}),J=l.useMemo(()=>m?(0,ne.Z)(m).map((Z,z)=>{var oe,$e;const pe=Z.props;if(pe!=null&&pe.disabled){const Ce=(oe=Z.key)!==null&&oe!==void 0?oe:String(z),ue=Object.assign(Object.assign({},(0,ye.Z)(Z.props,["disabled"])),{key:Ce,collapsible:($e=pe.collapsible)!==null&&$e!==void 0?$e:"disabled"});return(0,O.Tm)(Z,ue)}return Z}):null,[m]);return T(l.createElement(he,Object.assign({ref:n,openMotion:L},(0,ye.Z)(a,["rootClassName"]),{expandIcon:W,prefixCls:f,className:B,style:Object.assign(Object.assign({},u==null?void 0:u.style),j)}),J))}),{Panel:Ke}),Te=Xe,Oe=e(26058),Ye=e(71230),Ze=e(15746),xe=e(57210),cn={contentStyle:"contentStyle___LvtCl","h-section":"h-section___DJHpA"},un=e.p+"static/lunbo.fa8d4e84.png",o=e(85893);function vn(){return _jsxs(Carousel,{autoplay:!0,children:[_jsx("div",{children:_jsx("img",{src:carouse,alt:""})}),_jsx("div",{children:_jsx("img",{src:carouse,alt:""})}),_jsx("div",{children:_jsx("img",{src:carouse,alt:""})}),_jsx("div",{children:_jsx("img",{src:carouse,alt:""})})]})}var mn=null,Qe=e.p+"static/111.4ca6315a.webp",we=e(7485),ke={myservice:"myservice____U0_j"};function qe(){return(0,o.jsxs)("div",{className:ke.myservice,children:[(0,o.jsxs)("div",{className:"function1",children:[(0,o.jsx)("div",{className:"radios1"}),(0,o.jsx)("div",{className:"name1",children:"Name Analysis"})]}),(0,o.jsxs)("div",{className:"function2",children:[(0,o.jsx)("div",{className:"radios2"}),(0,o.jsx)("div",{className:"name2",children:"horoscope"})]}),(0,o.jsxs)("div",{className:"function3",children:[(0,o.jsx)("div",{className:"radios3"}),(0,o.jsx)("div",{className:"name3",children:"Qi Men Dun Jia"})]}),(0,o.jsxs)("div",{className:"function4",children:[(0,o.jsx)("div",{className:"radios4"}),(0,o.jsx)("div",{className:"name4",children:"Xuan Kong Feixing"})]}),(0,o.jsxs)("div",{className:"function5",children:[(0,o.jsx)("div",{className:"radios5"}),(0,o.jsx)("div",{className:"name5",children:"Eight house feng shui"})]}),(0,o.jsxs)("div",{className:"function6",children:[(0,o.jsx)("div",{className:"radios6"}),(0,o.jsx)("div",{className:"name6",children:"Personal auspiciousness"})]})]})}var _e=qe,De=Te.Panel,fn=Oe.Z.Content,gn=Oe.Z.Footer,hn=Oe.Z.Sider,en=function(){return(0,o.jsxs)(Ye.Z,{children:[(0,o.jsx)(Ze.Z,{span:3,children:"col-8"}),(0,o.jsxs)(Ze.Z,{className:xe.Z.mainbody,span:18,children:[(0,o.jsx)("div",{className:xe.Z.Carousel1}),(0,o.jsxs)(Te,{activeKey:["Fortune quick fortune telling","Our Service"],accordion:!1,children:[(0,o.jsx)(De,{header:"Fortune quick fortune telling",children:(0,o.jsxs)("div",{className:xe.Z.contentForm,children:[(0,o.jsx)(Ze.Z,{span:12,children:(0,o.jsx)("img",{src:Qe,className:xe.Z.img,alt:""})}),(0,o.jsx)(Ze.Z,{span:12,children:(0,o.jsx)(we.Z,{})})]})},"Fortune quick fortune telling"),(0,o.jsx)(De,{header:"Our Service",children:(0,o.jsx)(_e,{})},"Our Service")]}),(0,o.jsx)("div",{className:xe.Z.footer,children:"\u5E7F\u544A\u533A"})]}),(0,o.jsx)(Ze.Z,{span:3,children:"col-8"})]})},nn=en,an=e(93578),tn=function(a){X()(r,a);var n=Y()(r);function r(s){var u;return V()(this,r),u=n.call(this,s),u.state={currentComponent:""},u}return _()(r,[{key:"componentDidMount",value:function(){}},{key:"render",value:function(){return(0,o.jsxs)("div",{className:xe.Z.body,children:[(0,o.jsx)(ee.Z,{}),(0,o.jsx)("div",{children:(0,o.jsx)(nn,{})}),(0,o.jsx)(an.j3,{})]})}}]),r}(l.Component),rn=tn},7485:function(ve,F,e){e.d(F,{Z:function(){return fe}});var q=e(17061),V=e.n(q),ae=e(42122),_=e.n(ae),K=e(17156),X=e.n(K),G=e(27424),Y=e.n(G),l=e(67294),ee=e(27484),te=e.n(ee),g=e(23323),h=e(45803),d=e(55999),v=e(50457),i=e(44382),$=e(39539),t=e(37026),A=e(31622),H=e(93578),ne=e(69301),se=e(3184),c=e(85893),re=[{label:"female",value:"female"},{label:"male",value:"male"}];function me(){var je=g.Z.useForm(),Ie=Y()(je,1),ie=Ie[0],Q=(0,l.useState)("female"),w=Y()(Q,2),de=w[0],be=w[1],Pe=(0,H.s0)(),Ee=function(ge){be(ge.target.value)},Se=function(){var Ne=X()(V()().mark(function ge(){var ce,he,le,ye;return V()().wrap(function(O){for(;;)switch(O.prev=O.next){case 0:return O.next=2,ie.validateFields();case 2:return ce=O.sent,he=_()(_()({},ce),{},{Birth:ce.Birth?te()(ce.Birth).format("YYYY-MM-DD HH:mm:ss"):null,user:localStorage.getItem("user")}),O.prev=4,localStorage.setItem("info",JSON.stringify(he)),O.next=8,(0,A.cK)(he);case 8:if(le=O.sent,le.status===200){O.next=13;break}throw h.ZP.error(le.data?le.data.message:"error1"),Pe("/login"),new Error("addIndexInfo failed");case 13:localStorage.getItem("session")?(Pe("/setting/".concat(le.data.data)),h.ZP.success((ye=le.data)!==null&&ye!==void 0?ye:le.data.message)):(h.ZP.warning("Please log in first!"),Pe("/login")),O.next=19;break;case 16:O.prev=16,O.t0=O.catch(4),console.error("\u63A5\u53E3\u8C03\u7528\u5931\u8D25:",O.t0.message);case 19:case"end":return O.stop()}},ge,null,[[4,16]])}));return function(){return Ne.apply(this,arguments)}}();return(0,c.jsx)("div",{className:"setting-container",children:(0,c.jsxs)(g.Z,{form:ie,style:{maxWidth:600},initialValues:{variant:"filled"},children:[(0,c.jsx)(g.Z.Item,{name:"Name",rules:[{required:!0,message:"Please input your name!"}],children:(0,c.jsx)(d.Z,{style:{width:300},placeholder:"Please input your name!"})}),(0,c.jsx)(g.Z.Item,{name:"Email",rules:[{required:!0,message:"Please input your email!"}],children:(0,c.jsx)(d.Z,{style:{width:300},placeholder:"Please input your email!"})}),(0,c.jsx)(g.Z.Item,{name:"Gender",rules:[{required:!0,message:"Please select your gender!"}],children:(0,c.jsx)(v.ZP.Group,{options:re,onChange:Ee,value:de})}),(0,c.jsx)(g.Z.Item,{name:"Birth",rules:[{required:!0,message:"Please input your birth!"}],children:(0,c.jsx)(i.Z,{showTime:!0,style:{width:300}})}),(0,c.jsx)(g.Z.Item,{name:"Birthlocation",children:(0,c.jsx)(d.Z,{style:{width:300},placeholder:"Please input your birth location!"})}),(0,c.jsx)(g.Z.Item,{name:"Race",rules:[{required:!0,message:"Please select your race!"}],children:(0,c.jsx)($.Z,{style:{width:300},options:[{value:"Islam",label:"Islam"},{value:"Christianity",label:"Christianity"},{value:"Buddhism",label:"Buddhism"},{value:"Hinduism",label:"Hinduism"},{value:"None",label:"None"}]})}),(0,c.jsx)(g.Z.Item,{children:(0,c.jsx)("div",{className:"margincenter",children:(0,c.jsx)(t.ZP,{type:"primary",onClick:Se,children:"Submit"})})})]})})}var fe=me},57210:function(ve,F){F.Z={navs:"navs___gTJmV",body:"body___bBpz1",font:"font___MHPJU",cursor:"cursor___j1fvq",mainbody:"mainbody___ElL91",demologo:"demologo___EFjct",Carousel1:"Carousel1___VlJrX",contentForm:"contentForm___wsXq0",img:"img___YOXhy",newstyles:"newstyles___BRVg5",footer:"footer___mSewN",rotate:"rotate___tR8hT"}}}]);

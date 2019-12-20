#!/usr/bin/python3

import re

# regex along the way:
# [,\.!?:;><!@#$%^&*\(\{\[\]\}\)-_=+|/~`]
# ([,\\.!?:;><!@#$%^&*\(\{\[\]\}\)_=+|/~`]|[-'\ ]+[-'][-'\ ]+)

def main(text):
    # print("Text:", repr(text))
    d = {}
    regex = re.compile("([-,\\.!?:;><!@#$%^&*\(\{\[\]\}\)_=+|/~`]|[-'\ ]+[-'][-'\ ]+)")
    text = regex.sub(' ', text.lower())
    print("After", repr(text), "\n")

    for w in text.lower().split():
        if not w in d:
            d[w] = 1
        else:
            d[w] += 1

    print(d)
    results = sorted(d, key=d.get, reverse=True)[:3]

    if len(results) > 3:
        return results[:3]
    else:
        return results
  
if __name__ == "__main__":
    s = """XhIZSbkpmj!'NekkM/-/'NekkM!zHrTlGkfgS.!hBC;;!-qBkglucGNt?-!!.hBC   ;BMnnkvtpN? _,!zHrTlGkfgS?,zcHVbxdnOC!._KpltvH ;,.'sD,'NekkM?-BMnnkvtpN;_--hBC//;.!hBC,TFpDmpMuT;;:,/hBC.cj'g ,_; DGYckbjzhC, .qBkglucGNt?:,mgmMTud!::.'NekkM 'NekkM:._-?mgmMTud,TFpDmpMuT/?mgmMTud/zHrTlGkfgS;qBkglucGNt!zHrTlGkfgS ,_  hBC:;?qBkglucGNt?,cj'g!?;?-'NekkM 'sD?;;_djm,; mgmMTud ?_ -TFpDmpMuT!-/-_'sD!?/,zHrTlGkfgS:_/bVEocQmwe:??_!zcHVbxdnOC   ;:zHrTlGkfgS;-_-?qBkglucGNt/-!!/djm-!?,cj'g,_ !.'sD/djm-'NekkM!--'NekkM:./'NekkM.?.,'sD;!-'NekkM?-,KpltvH:cj'g!_zHrTlGkfgS;?-;?BMnnkvtpN,.,!!djm;,/KpltvH,,!:,'NekkM:;!vlCx-;-;qBkglucGNt;-!zHrTlGkfgS-_:,/qBkglucGNt:?UPyxqyuFcV,,_zHrTlGkfgS,_zcHVbxdnOC;:DGYckbjzhC ?!::BMnnkvtpN__-bVEocQmwe! zHrTlGkfgS.,,bVEocQmwe_zcHVbxdnOC--;,BMnnkvtpN,;;;zHrTlGkfgS/:?_-zHrTlGkfgS!.;cj'g:;aFvXrhssXk_:;'sD,/?UPyxqyuFcV-DGYckbjzhC:hBC/:-;_mgmMTud!;-.qBkglucGNt/vlCx ./djm,;:! hBC !;lZZ?,;-qBkglucGNt;/;/djm?/UPyxqyuFcV .; ?TFpDmpMuT,hBC.?/djm?//:BMnnkvtpN- ;:aFvXrhssXk-!_- DGYckbjzhC:/;__hBC;  !,'sD_/.;'NekkM:'NekkM.hBC- zHrTlGkfgS_;DGYckbjzhC,?/mgmMTud ?zHrTlGkfgS??'NekkM,??qBkglucGNt;:-/ hBC:- 'sD-,._?'NekkM,djm -_-!zcHVbxdnOC?,!KpltvH:!,zcHVbxdnOC:  -.qBkglucGNt!-'NekkM-.-?'NekkM.XhIZSbkpmj:qBkglucGNt?-zHrTlGkfgS zcHVbxdnOC__ :djm _?;-hBC?_mgmMTud 'NekkM?_,,:vlCx .zHrTlGkfgS-::?KpltvH-/!zHrTlGkfgS/hBC/. /qBkglucGNt!.hBC;!;'sD;,..DGYckbjzhC:.:'NekkM;,/ DGYckbjzhC?:.?BMnnkvtpN-?:qBkglucGNt/?;!mgmMTud?,!,'sD.!TFpDmpMuT!:!_lZZ?!BMnnkvtpN- ?mgmMTud:/:TFpDmpMuT?;hBC_. ,;DGYckbjzhC,/; :'sD,!DGYckbjzhC!;?mgmMTud!,:?XhIZSbkpmj;: 'sD;-zcHVbxdnOC-/?'NekkM!-?-_mgmMTud?,?BMnnkvtpN.  'NekkM.!?!.djm:?-; 'sD_;_./'sD_zHrTlGkfgS- cj'g;!:aFvXrhssXk XhIZSbkpmj;/!XhIZSbkpmj_'NekkM_bVEocQmwe;,qBkglucGNt?'NekkM-; /?djm,qBkglucGNt-::mgmMTud,-/hBC?.,'NekkM:.;..djm_!:BMnnkvtpN_.mgmMTud/hBC-!_:zHrTlGkfgS_?.-'sD.., ,TFpDmpMuT_?:'sD;;!zHrTlGkfgS,qBkglucGNt.vlCx:;-/zHrTlGkfgS?;?!,djm..;!/zHrTlGkfgS.//aFvXrhssXk;zHrTlGkfgS.;,-'NekkM-!!/'NekkM:- . bVEocQmwe?.-djm/'NekkM;,;qBkglucGNt!/-qBkglucGNt.;XgpA,!'sD_/qBkglucGNt-_-_ 'sD!UPyxqyuFcV/djm?bVEocQmwe?./mgmMTud,! ,-zcHVbxdnOC! ,-hBC/zHrTlGkfgS/'NekkM!,cj'g._:!BMnnkvtpN! zHrTlGkfgS;?djm!/-qBkglucGNt/-cj'g;. djm?aFvXrhssXk-:;KpltvH_!zHrTlGkfgS-:/!zcHVbxdnOC?! ,qBkglucGNt:?_lZZ/??-;zcHVbxdnOC/vlCx hBC.zHrTlGkfgS/_,zcHVbxdnOC,?mgmMTud.'NekkM_- 'sD_/!cj'g.zHrTlGkfgS;:TFpDmpMuT._;KpltvH/'NekkM;lZZ--?:."""
    print(main(s))
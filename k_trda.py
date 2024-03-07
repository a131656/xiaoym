# -*- coding: utf-8 -*-
"""
先运行脚本，有问题再到群里问
new Env('天瑞地安');
cron:6 9 * * *
抓包 https://crm.rabtv.cn/v2/index/userInfo，在请求头内找到Authorization Bearer后面的字符串Bearer xxxxxxxxxx 取xxxxxxxxxx ，https://crm.rabtv.
多账号用&连接或换行，或在环境变量添加多条
示例：trdav2ck="xxxxxxxxxx#accountid&xxxxx#accountid2"
"""

import sys
version = sys.version.split(" ")
ver = version[0].split(".")
if int(ver[1]) != 10:
    print(f"\n【python版本为{version[0]},请使用py3.10运行此脚本】\n")
    exit()

try:import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads(gzip.decompress(marshal.loads(bz2.decompress(marshal.loads(lzma.decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xe5\xa3\x01\x0fP\xf3L\x0f\x00\x00BZh91AY&SY\x10\x97\x19\'\x00\x06e\x7f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xe0\x08\xbfKz}w\xc7\xd9{\x9c\xed\xec\xbb\xbe\xf6\xfbw\xcf\xaf\xbd\xdc\xab\xef\x97\xbd}<\xfb}\xf6\xbd\x1dM\xa40\x13L\xa7\xb4H\xf4\xd3\xca2\x9b\xd2\x9f\xa4\xd1\x1ej0OTxOMF\r\x06*~\x94\xf12O\xd4\xf4\x9azF\x11\xe94\xc8\xd1\x94\xf2i\x8d\x14zda14\xd4\xf2hm$\xf4j<\xd4\x8f#\xd2\x0fT\xd3\xcd\x04\xd3\xd4\xf51\xa6\x99S\xcc\x98\x93i\xa2mOS\xd3LiE\x1b\xd2i\xa3G\xaaz\x03L\xd3JyOd!\xa6\x8d\x94\x1eH4i\xa8\xf4\x9e\xa7\xe9\xa4\xd3\xda\xa0=\x06\x99\x08\x19\xa3SM4\x9ei5\x1f\xa1\'\x91\xa8\xf3D\xda\xa7\xa9\xb5\x1e\xcai\x90\xc6\xa62\x13\'\x94\xf156\xa7\x93I\xedI\x93\xd3MOQ\xfa\xa7\xa8\xd1\xa7\xa4i\xe8!\xe9\x1e\xa9\xb6\xa7\xaa2M\x8a\x06i\x18\x13\xc94i\xa7\xa4\x0cOQ\xa1\xe54zi=M2f\xa1\xea\x1af\xa7\x94zi\xa8z\x81\xea=C#!\xb4\x98Lh\x1a\x9e\x93i\x93\xd5<\x93\xc8\xc5\x1eDhi\xa1\xea\r\x06\x9e\xa3\xd24i\xb0\xa3G\x92m#\xd4\x03#i\x03\xd0\x03PBd4z\x83A\xa7\xea\x9e\x88\x0f$\xdajh\x01\x9a\x8d\x1ej\x80\xf54\x01\xe5<\xd2\x9bI\xeayM=M=C\xda\xa1\xb5<\xa6\x9bj\x9b\xd2\x9bSji\xea=M\x06\x9f\xa9\x00\xf4\xd4\xf4\x86!\xea\x03!\xfaQ\xb2F\x87\xa6\xa1\xa6\xcab=LG\xa8\x004\x0c\xd1\r\xa46\xa2\x13C\x10\xc1=\x1a\x9e\xa6\x9a2=L\x98\xd1\xa6\x98\x8d4\xd4dzOLM\x18\x934LG\xa9\x9a\x8c@\x1bP\r6\x9a\r\x1aFi\x06\x1a\x1a\x9ahz#\xd2cM\t\x90\xd1\x8dOH\xd1\x83I\xa0\x06\x834\x9bSM=G\xa9\x83Q\xa3\xd0\x98:\x9bM4\x06\x8d\x13\xd0\xd0\x1a\x984\xf4\x93#\x1a\x1a&O@!\xb4\x014\xf5\x0fA26\x93\t\xa6\x8d\x0f\xd4\x8c\'\xa3SL\x9a=\x02cA4\xc1\x01\xb52h\xc10\xd4\xc9\x91\x840\x8fQ\x84\xc2i\xa0\xc6\xa6&i\xa4\xcd&\x99\x02\x14W\xd0\xe4\x8a\xeb\x01*$\xe8\xe4dF\xb2z\x96\x985\xe3\xfb\x96%\xea$\xd4LG]\xa0t\xcc\x01\xbaV\xef\x1eHzeU\x82\xacb\xdexux\xae\x8fI\x84\xcc\xef*\x94-\xec\xc1\xec\n\x8b\x08\xaa\xed\xdc\xa3\xb0\xdbe\t\tAQ\xcaX\xbe|U/\x93\xd6\x08/\x88\xad-\x0c\xa6z\xa9\xa4\xd0B\xbc\\(\x9e\xcd\x03\xfc\xa7\xc2\x99u~\x03\xce!w\xac\x9f\xe72\xcb1E\xd8/i\x85\xbe0CHd6z\xd5\x06-\xfdL(\x86b\x90}p\x90\xc5\x07+7\x1a\xd5\xcf\xa2H\x1bz\xc1\xd5TW\xbf\xa1\xab\x16&\xa68L\x0e\xb0\x15\xd6\x8b\xacT\xb4\xdf\xdb\xc2B]\x89K\x8f\xad\x7fj\x81\x99\xaf\xde\x11\x15\xa3\xcf\xa0f\x0f\x89\x0f\x92\xe8z\x1c\xadP\x18#_u\xf7\xc0\x93\xd8S\xa1\x8b\x97$\xfa\xd3q\xd7`mz,\xb3C*j\x12\x1a=\xe5ir\xd9\xfe\xd7 \x9b\xf2y\x9c\xc1WK"\x8a\n\xfd\xbbH\xa8\x97\xdc\xbb\xa9\x89z\x17\xfe\x05\xb2|a\xebB\xaa\x87\xd2\x1fL\xb2z1\xdd\x12\xb1\xe5\xd2\x00~[\x95\x86Zn\xc3}\xcb)\x01\x1c \x97\xf3U\xf0\x0f\xef\x90\x0c{\x91\x9d\x9a#\xeeBa\x82\x0b"\xbex2-5\xbb#\t\x89)m\x18\x88n\x13\x9b6\x9d_\xe7\xf0\\\xbb\xc5hR\xca`\xf9\xa8\xc7\x0b+\x89\x1c\xb41]\x14\xa9r\x86HX\x1c\xce>\xbd\xcf\xdd\xa8\xce.*\xacO\x8e\xf1\x0c\x8fQ\xb6C\xbewy\xdd\xe96zX8\xac\xae\xcb\xec!\xa4X\xb8\x03h~\xb7-Q\x12u\xac\x90\xff\x02\x1c\x9a\xb6\xd1\x17\x95\xfc\xfd\xce;\x12\xa1\x0e \xb2\x15&>\r\r\xad\x8f\xb9\x8d\xd8\xd8\xd6\x9d\x14\xf4\x08\x91v\xc8\x9eU\xd6\xa6\x98(Q\x18v\x90\xc8\x02\xc2\xae\xa4\xfbHO\x1cP\xc1y\x98\x99` \xa8\x14\xde\xb0w\xba\x88\xea?Q\x00\xb5\x81\x85y\xf9\n\xff7\xcf\x93\xaa\xac\xb9\xd2s\x11h\xfe\x90\x14\x15q\xc0\xde\x84s\x9fm\xa1=\xa8\xe3\x9c\xb0\x98\x9e\x9e0b\xb6\x1f\x14\xc4M\x05\xe1\xe7\xe4\x0c\x10\x14\xab.\xe6\x1a\xa0\x98\xe3A|z*\x90\xf3<\xfe\x13\xa7g\xf5e\xab\x85\xaa\x8c17L\xea\xab`\xf1\r5j\xbf\x07\x9aI=z\x88\x89\x10l\x8e\xcc\xd9\xf1\x1c0\xc7\x03\xf1\xb1EytY\x97\xa9\x1b\xec\xf6\x07\x1fP\xb7v\xc9\xc5\xffq\'\xb2\xa9\x84NXK\x05\xca4/\x17\xfd@\x81h\x8dq\xb8\xad\x8b\xaa\x89\xacO}\x82\xc9\xd8\xf2(#\xd4\xca\xe4\x9f\x15g\x8b\xdde\xbbN\x91\x08\xf7?\x86\xe1\x17\x89\xaej\x81\xee=\x98\xc7\x1f\x99lJp\xe9-\x0c9\x0bf\x01\xd4\xf5\x9e\x19\xda1^t\xef~\xc14\x82\xe6[l^\xac9\x88~\xb8_P\xf1\x1c\x8a\x9b\xac\x91\xc2\x0f\xc4\xfb\xee5\x07\xa5\xc6s\xacYV\xbe\x9c\x97\x86\xde\xbbQ\xe3\x873\x9c-\x01\xc4\xe0,\xdd9\xedcg\n\xa2,T\xbe\xd0C\x97\x85xj,\xea\xcf\x8f3o\xab\x11\xe9\xa4\x8edL\xfen\x97\x06Q4\x02k_h\x02\xdc\xc9\xc5\xa5\'\xaa\xc7Wtq\x85\x03-\x97\x93\xcc\x82\xcf\x9e)\xf5\xablq\xb3\xf4\xf4\xfb64\xef\xaah\x8c\xa1\x05\xca_\x8a\x846\x92O\x1fz\xc8D\x13\xc4x\xd6S\x0c\xdf\x13ia\xddW\xedp\xf0\x8f\xf3\x91\xfe\xbaO\xb1\xba<\xfd\x15,\xa3\xa2\xf0n\x02\x91CUCg|\xa7^"\xa8U\x11\xab\x95\xe1\x9c\xbe\xa2\x88g6\xd3\xe2Oj\xe8E\x01\x1f;\xc8;\xc3ZQ\x19}\xbe8\xa6(\x88\x80:\x16_?\xfd\xde\x81\xfe\x94\xd3\x90\x94\x9cr\xa3\x98\x0f\x8a\x1d\xeb9T\xa0\x87h\xd2\x03\x84\xafj\xc7\xa2)\xf7V\x94N\x13\xce\x992\xcbf\xd3q\xac\xdd,G\xd0,\x11xD\xbe*\xe5\xa0\xdc\x08{{\xbe\x1a\x8c\xc0\xca\x83\x9c\xbd\xe4d\'HW9M\x1aU\xc1\x96\xd9\xa7R\x18\xc3\x13\xd2\xd5\x12\xa1\x08\x1f\x03\x85p\xd3k\x1b\xad\x93\x83C\x1a\xd8F\x83"M\x827\x91GN?K\xf7 9N\xf1%\xde\x17oWx\xabju\x1d\xa1\xa7\xdf\x13\xe9\xcc\x9aK\xb8\xd0@_\x0bZ\xebUx\x98\xb2\x85}J\xb8.@\x0e\xb6\xc2#\xd1\x85\xd3dz`\xa4\xa6\'\x8b\x9c6v\xc0j3\x952\xa7\x06\xb3-\xf8\xce{\xdb|\xb5\xc4\xad\xed\xda\xec\x1a\xf5\xed\xe3\x89\xbc\xa1\xa9\xd8\xf2 \xb0\x84\x89F \x0c:\xb5p\x11\x8fMSj\x1fm\xd1\xfe\xb1\xab\x7f\xd2z\t\x8fO+\xa4l\xd7\x1c\x005C3\xc9\xda\x89\xca\xc9\t\x11.\x112\xc8\xc0|\xdf\xa3~\x9d\xfe\x8dt\x86\xf1\xa2\xcaz\xed\xbaX\xcd\xf7\x8cX\xf4\xe5\xef\xef\xa0\x88\x87\x02Z\x12y\x1a\x8a\x01m\xecd\x85)\x8b\x98\xd9\xbf\xe0\xac\x94\x91\x07\r9\x93\x03\x91\x87\xd3Bg:\t\xf4\x84\xbb,\xe3\xbd%\x81^\xfbC\xa4\x7f\x9c$\xf8\xc7\xef\xa1\x186\xf5\xae\x9aSi\xfd\x81s%\xec\xa1\x939\xe8\x1d\xcf\x08\xce\x1cFz\n\xda\xf3\rt#\xe7\xec<\xd4P5\x13\x80\xc6p-,\x0b(\x80\r@O\xacd\xd7O\x15tB\xff\xc1\x94\xcc\x06\x1b\x88\xe4\x8a\xddY\x88k\xc6fZr\xedj_\xa0\xcf\xab\tz \xac\x7f\xc0\x8e6E|\xefF\x03(\xbd\xdb\xc2-\xa6\xc74\xa8\xc0]\xc2\x9d\x8c\x15t\xdbvb\xd4\xa5N\xb1\x1d\xedpd\xa9MG\xb1\xdd#\xb3\x822\x9f\xd3Q.\x80s\xc8\xc9\xf641\xcb\x0f\xcd\xe4\\\xa2\x19\x92\xf4a\xaf\x85^Z(\xe0\xba\xc8g\xe0\xec\xed\xde\x1e\xec\x9f&\xdd$\xe0I\xe3\x86\x94[LU\xdd~\x03t\xfa[\x1aB\xfa0\xbd*\x1dObfY\xbc\xf1%\xc2\x95Yx\xb56Aq;\xf6\x00\x13ZK\xcaR5uU\xa1\xab\xdf\xaf\xa4"6\x90\xb1{\xce\tX\xd3\xceT\xf9N\xa0 \x8ak\x1b\xf4\x01\x13\xd3\x9c8\x12C\x03\t\x16d\xf9\xb0\xf6\xf7QS\xec\x15GU\xd7\xcaW13\xbeaU\x97\xb7\xe8:\x98\xeb\xce\xffB \xd4\x8fk\xd6h\xc3\xbbx59\xab\xa5{\x0fiA*I\x87\x11\xa2K\x9b~\xf9\x1bXs\x1b"|\x17\x8f\t\xfc\xea\x0f4B\x94\xca\x0f=\xce~\x16HOX\x94\xd3\x8d\x86wL6\x99\xb3\xf8\xc4ex5\xa7e[\xcb\xb1lm\xc0\xb5\xdf\x15E"\xd6>Y\x03,\xedb\xedp"\xdaE\x16\xea\xe7\x93\xfb\xe8\x9e\xf1\xeb\x14\xe5[\x0e\x87\xe37\x90\'\x036f2B\x96^E\xde\x85)A\xe8\xa0\xd0 fql.!\xf2\x18L\t]\xdaXm\xa8^\xa6\x92\x1b\xa5WB\x14\xb1\x87\xda(\xf7\t\xf73\xde\x82|c\x1a\xb7k\x9b=m&pIM<\x08\xedWW\xd5]\x83_\x8801r\xab\x7fXFh\x9c\x9dE\xbb\x99\x04g,\t\xee\xf2\xbc)\xbf\xa8*\xa3\xd2P\xfdx\xfc\xbc\n\xd4~\x07\tq\x8dg\x8eh\x0cU\x8e\x9b\xc3H\xc1\x85\xea\x97\x0c\x1bIb\xa2 T\xe78N6\xd7N\\\ni`\xe2Z\x04\x15Cb\xa9\x0cW\xd3\xfd\x088\xb1L\x8d\x9d\x80\xeb\x83\x14\x88\x95\x8aT/\x86rB\x05#\x82\xf33\x1b\xf9c\xac\x1f,\xdc\xca\xdb\x16\xef\xa3%X\xca\x0fY(\\\xe1\xe1\xe2f\xcf;q\xd0\x83\xba\xb0\xc4V\xe5\x17\x01\xce\x9f\x0b\\\xa4V\n\xd6\xb1\xcbe`\xfax\xf9\x88\x0c\xdb\x91\xf5S\xb3\x8fQ\xb4u\x7f\xacTY\x89\xddN\xddQ\xd0\'\x17\xcb\x1a\x1a.+\xaf\x8a\xdd\xe6\xd6`d\xd6.W\x15\xd8\xe70$\xc8\xf6\x98e\x8f\x8d\x0fG\xf0\xb8jF\xcdeU\x15\xf6\xf6\x1c\xd4\x03o\xc20.\xabM\xaa\x13\xac\xcdP\x84\x0cZ\x88\x89\xab\xd3A_Z\x19\x87\xd2\xf6\r)\xe8\x1c\x9c\x18+L\xa89\xb58\x1b\xed\x1c\xb6:\x88\x19\x06\x83\n\x1b\xafr\xa9E\xcaY\xa36\xc3&\x8e\xb7jB\x8f\xc0n\x91*\xcb\x83a\xe1D8\x87\xc4\'\xe6\xe6\xda\xec!\xff8_\x8a\xe1\x0c\xa6{\xcf\x13\xa9NjerR\xe4\xa6\x08\xd5\xd4\xce!S\xd1\x1b\x1d\x9b\x04!\xba\xb0\xc7\xd6UQV\xda\x93$\xd6\xe0DI5\xa2\n\x0f\xd1\xa0\xb9\x8bL\x19aQ\xc1l\x81\x9c(\xbd2\x06\xe8\xb6A%\x82uO\xd8\xf0\x0c\x00{\xb6\x1f\xb5\xf1\xef;\xd9;/;|\x96D\x16\x98\xd1\x11\x82\x1d\xdc\x80\xfd\xdc\xd2\x9aI\xb8\xc2l\xb3\x1a\x9bt\xeb\xb0R\x12\x89\xd8<\xdc\x0f\x0b,z(D}\x8e\xec\xcc\x10\xd6\xad\t\x14X\r\xc9\xf4\xbb\x0c=\xb9\x87\xb4\xa5S\x02\x02\x90\xedj\xd2h\xe7\x13i/\ne\x0c\x92+x\xd6\xb5z\x08\x94\xe4\xf0\x8f\xc8\x8f\x91\x99\xecG\x11\xa5\xaeE\x7f\x0cOc\xadz\xedi\xd1\x8e\x8d:]\x82\xbf\x80\xf9!x\x96\xc1\x80\xa8\x15\xa0s\xa1\x19\x1b\xb8@\xaet\xeb#\xb2\xff\x1c\xf1k\x12\xf8\xdd\xa1O]\xb1\xce\xf0!\xac{\xf5`&\x86\xac/>\xa1\x8e\xee\x8d}oY\r\xde\x0f\n\xb9<\x9c|\xbe\\\xebq\x99\xe4\xe4\xcfD#,v(\\&\xf1j\x17\xea\xa7\x01\x8by\xe6\x9d\x9c\xfb\xd6X0a\xadG\xab\x95;\xae\xb4\xd7\x91\xe7pI\xd9s(\x99d\x1b\x8fs\x9b\x05\xe4$\xb1O\x18\x1c\xc7\x8b\xb6O.l4$\x0c\x11k\x80\xdd\xc1Q\x8dE\xd6)\x9d^\xf9\x1f\x13\xc9\xc4\x07\xa0\xf9$\xeaK\xa4\x90\xb5\xd3\x86\x84\t1`\xa0\x8b?\x1a\xdav`HMv\xb0\xe7\xaf\x94\x11H)\x1a\xf1\xb1\xd1\xcb\x04g\xa7\xa1\xcd\xe9\x14\xc8\xb6\xbfR\x88m_-\xa0{\xe7n\xad\xcb\x9b\x8c\r\xeel\\\xc9\x1a\xcb\xd9HI\xa5L\x9e\xb3\xa4\x18+\x00c\x9a]\xea\x04$\xc8#q\xb2\xec#X\x10\xef\xc6\xce\x02cyG`\x98 \xa3p\xa6\n\xe9\x08\xcc\xdc\\\xec\xe6\xde:(\xf9\\\x98z\t\xea\x91\xc1\x86\xc8\x13\x02\xe0\x94T0\x97\x9c\xb4N\x9c\xb7\no\x88\xf7\xc6\x99{s[Q\xa6ZNr\x0fF+\xad\xf3\x16\x14\xe8\xda\xf6\x1d\xa8\xbd\x1b(\xffA\x05\n\xa7g\x7f\x86\xf3\x89\xea\x19j\xaa\xc8\xd2 \xa7\xbb\x85\x95\xf0Q\xc2E\x84\x89\xdd \x92\x08\x9e\x9d\xf7\xdf\xc4\x87j\xb5\xd6\xd0\xd1fI\xb4\xac}=\xf9u\xcbp8\x96\x82C\xa1tz\xdbv\xd4qp]m\xa2\xb1\xa8A\xdb\xa0\xa2\x1fkxX(\x01t\xab\xdb\xb3\xa9\xc4J\x93M\x7f0\x03\xa7"\x04\xbei\xa8\xa4Q\xaf[\x9f;\xa7\xe3\x7fB\x14j=*G\x9c\x7f05T\x08\xd2\xa9\x89\xef\\\xc4\xa6\xce\x162\xd0Sm\xca\x82\x9d|\x83\x06\xb6T<\x1b?\xd2\x17\x13\x17\x01|\xdf\xbfs`\x93\xf2\x02:?7N\xb6\xa4\xf80\x82\xd7\xc8R\xfdA\xafG8xw*\xd23q\xab\xaa7\xa8\xcdi\x8c\xf7\xd0T\xeeGy\xceCGo\xbb\x0f\xa7\xbe\xe2`\xd0MI\xbbk{\xab\xf8WG\xd65\x997\t\x8by\xa2\xc1\x1e[*\x03\x91j\xce\x14\xea1\xfb\xbf\x82\x7f\xa6!Eu\x9c\xc3Ao]\xb2\xaf\xd0I\xaf\xed@\x80ro{\xa7:lt\xab\x13t\xfeJQ\x8d\xbbs K.C\xa5\xb6o\x02|\xd1h\xa9\x0f\x7f\x98\x10\xbaN\xe6e\x11\xe0i\xac\\j\x884-O\xddjW\x97\x85\x9b\xa3\x87\xddj\xdc\xb2\x05\x96\x9dj\x9eo\x91\xa7=~\x8a\xec\xb7\x1d\xf0\xcc3<%o6\xfd&&Kf\xfc\x98\xc6e\xdb\xdc\xf7$8\x94\xe1\xc2\x86\xf9\x1b~\xf0\\4,\xc7\t\x1d>C\x86\xb7>\xbag[\xa8a\x88K\xc5{\xe7~79\xce\xf6W\xc5\x9b\xd0\xb0\x8d4\xa2\xd0.i\xf4\xf6>V\xd4\x17R\xafL\xd1\x05][4\xd4\\\x8dY\xcd\x86g\x0b\xf8\x8es\xa8\x02\xf9\xb1\x88[*sf!7m\xea\x99\xfcL\x03\xa5\xc1\xcd>\xfc\xf7QUP\xea\xef|0I9T\xff}\x8aB\x19\x891\x83p\xb8y\x16\xfe\x91%/V\xacQ\x91\xa5\xcdw\xa0[D\xae2\x15\x1e~\xbaS\xc2#e\x0c^\x9c\x1f*V\xb7&N\xaf\xa8\x12!9\x15\xe7\r\xe0l7\x94\xbc\x9e\x13\x0e\xa9l\x0f~\x0e\xc1\xff\x11\xc2\x0b\x11\xfb\xb1\xcc\xf4s\xaa\x92\x0e\x83\x98\x13\x9e\xca\xf94\xea\xbbB:\xa4[\t&\xc9\xff\xfd\xd5-\xd4\xd8\xba\xe0\x03\xab\xe0\x10\x0fC\xd9\xd4~3\xea\xad$\x99\xee\xd7\xc8D\xd9\xc8bI\x1f`\xc7\x077;d\xb2S\xb9\xec\xd3~\xee>\xdd\x05o\xe5\xbe\x9b\x10\x96\x04h\xef\x9fFP\x87\x13\xf3]^<\x95\xe8\xd3\xcd\xa0Q\xe4\xb3*}\xe9\xd2\xcf\xab\xca\x93R\x93\xe6MU\x01\xe4\xa8\x1c]\xa9x\x13\x96]\xe4\xca\x88\x11\xa6\xfb\xbb\xe4\x86S[\x1f\x8a\x127?\xfb\xcf\x03S\xa2\x08:\xc8=6\xb9\xcah*\xe1\x0c\xe8\x1doL\x0bE\x0e8M[\xfb\xce\x19C\xf7\x881\x8d\xf7\xc9mA\xa8\xed\xfd\x81\x17\xc1\xc3R\xe1"\xb6A w\xfd%%6\x93\xa1\xcc\x85g\xf6-`?g\xcb\xac\xa7jO\xd5\xa43\xee\x81\x8bU\xff\xb1\xc0]}\xc6~+\x9db\x7ff\x91\xda\xfe\x94gv%E\xef6\xe4\x7f\xea\xc9$\xf1\x7f{|\xcb\xf1ZX,\xd2\x94\xce\x9b\xae\xc3\x15*ac\xf5\xc7\xa49,l\xa0\xc9\x01\xa6\xff\x03\xa1\xa5\xfe\xb4.\x86\x83\xa638\xd6\xa0C\xef,\x9eu\xed`\xb1\xdd\xc8$\x10\x0b\xd1\xe1\'\xcc\xc9\x0bd#\xa2."\x11QM\xb8\xc8\xf7:\xcex\xf4_\xd6\xb3k;i\xbd\xee \x11\xe0\xbcoU\x95\xd8\xfa\x0b\xb9"\x9c(H\x08K\x8c\x93\x80\x00\x00\x00\x00\xe5\x1d\xfc\xbf\xf6y6b\x00\x01\xe9\x1e\xd1\x1e\x00\x00\xf2\xe7\x9e\xa5\xb1\xc4g\xfb\x02\x00\x00\x00\x00\x04YZ')))))))
except KeyboardInterrupt:exit()
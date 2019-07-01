import random
from Crypto.Cipher import AES,PKCS1_OAEP
from Crypto.PublicKey import RSA


def decrypt(private_key, ciphertext):
  """Decrypt a message with a given private key.

  Takes in a private_key generated by Crypto.PublicKey.RSA, which must be of
  size exactly 4096

  If the ciphertext is invalid, return None
  """
  if len(ciphertext) < 512 + 16:
    return None
  msg_header = ciphertext[:512]
  msg_iv = ciphertext[512:512+16]
  msg_body = ciphertext[512+16:]
  try:
    symmetric_key = PKCS1_OAEP.new(private_key).decrypt(msg_header)
  except ValueError:
    return None
  if len(symmetric_key) != 32:
    return None
  return AES.new(symmetric_key,
      mode=AES.MODE_CFB,
      IV=msg_iv).decrypt(msg_body)

n = 767185100488428919016632170568302864430595686111633853865853178271740753807631107438469636874149151975213091797469800231881024440218931836348027417405438325824297104749723127225412009768596670293358224481910117990221965588027812122211776093837448747674231104831266261442032627678816332117512253254417902273087090526668802909231100189062059172214484966826827211424626065276059613985574544412609131190663177251147222337439529271810128210037468960468152611646862922563271251560265472129891502660301505695797093180509246596535280995459316546041298821485677298673720375230145667734470085748234479066650224747956677855856599512299156493819425327975989659334858931601551091941865956355246897792662048547218085830897307455941801348993015738325478197038027303177775403199123814405059965177746759645789493365730861927684438829511689481413687211445070334362680691231035336073760204340782163790243228692508230246815979346673469404207207020959641247494823624451087045877926954318590208564006401609051341418752333546705485665209085221084705978680432756976392471120062576376133959869719109290112050140002435438961179172972247159977728102448723565655241549851208603332382646287005177858241486292754465516995791462277418258182436844243511176521576921
e = 65537
d = 721191688220259225212882413970306893386028335596160008376451204769296799679273345851492094367190761781725256869532011729034379872636952447834494608107088276506146085866318910266005204660324757975391206400682340496842926224075216278212660048356463409169080517973734712222420100493408556831952864771017564478696758673222936808702101415196535414831163920171310417648784085776393193134004860341059605328202038910671499668354891425876655610784570360506613761666538458172910192198679146237672699328560281412128527651018717126498704419919397802287445836612747104943628253920362761459713338156724137301649252273862322189657902670565501638115915842312168192035306801439995555033844235943336091071308455141527109573245515241442867919003222667328858661835219509364430813502407540126021720418496926414892357844928915642165007862585242257219987365006546161661900139407261272997093588897070572627082597614555368108495336373604358767710689650722126937657272222443989617551733439301604282493241228268787747840047648117273651708763236784358192582507075928163197505184961282609141019215899581197040983910800452824799702184076199741463576373022568563200083869329095884398213316589495136460272142045132620619486975289393170586048926615322883432900453921

if __name__ == "__main__":
  k_text = open('/home/jun/PycharmProjects/Crypto/rsa-buffet/key6','r').read()
  k = RSA.importKey(k_text)
  private = RSA.construct((n,e,d))
  c = open('ciphertext-3.bin','rb').read()
  print(decrypt(k, c))
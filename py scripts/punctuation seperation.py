s = 'bla.bla'
import re
s = re.sub('([.,!?()])', r' \1 ', s)
s = re.sub('\s{2,}', ' ', s)

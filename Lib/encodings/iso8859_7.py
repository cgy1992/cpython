""" Python Character Mapping Codec generated from 'ISO8859/8859-7.TXT' with gencodec.py.

"""#"

import codecs

### Codec APIs

class Codec(codecs.Codec):

    def encode(self,input,errors='strict'):

        return codecs.charmap_encode(input,errors,encoding_map)

    def decode(self,input,errors='strict'):

        return codecs.charmap_decode(input,errors,decoding_table)
    
class StreamWriter(Codec,codecs.StreamWriter):
    pass

class StreamReader(Codec,codecs.StreamReader):
    pass

### encodings module API

def getregentry():

    return (Codec().encode,Codec().decode,StreamReader,StreamWriter)

### Decoding Map

decoding_map = codecs.make_identity_dict(range(256))
decoding_map.update({
    0x00a1: 0x2018,	#  LEFT SINGLE QUOTATION MARK
    0x00a2: 0x2019,	#  RIGHT SINGLE QUOTATION MARK
    0x00a4: 0x20ac,	#  EURO SIGN
    0x00a5: 0x20af,	#  DRACHMA SIGN
    0x00aa: 0x037a,	#  GREEK YPOGEGRAMMENI
    0x00ae: None,
    0x00af: 0x2015,	#  HORIZONTAL BAR
    0x00b4: 0x0384,	#  GREEK TONOS
    0x00b5: 0x0385,	#  GREEK DIALYTIKA TONOS
    0x00b6: 0x0386,	#  GREEK CAPITAL LETTER ALPHA WITH TONOS
    0x00b8: 0x0388,	#  GREEK CAPITAL LETTER EPSILON WITH TONOS
    0x00b9: 0x0389,	#  GREEK CAPITAL LETTER ETA WITH TONOS
    0x00ba: 0x038a,	#  GREEK CAPITAL LETTER IOTA WITH TONOS
    0x00bc: 0x038c,	#  GREEK CAPITAL LETTER OMICRON WITH TONOS
    0x00be: 0x038e,	#  GREEK CAPITAL LETTER UPSILON WITH TONOS
    0x00bf: 0x038f,	#  GREEK CAPITAL LETTER OMEGA WITH TONOS
    0x00c0: 0x0390,	#  GREEK SMALL LETTER IOTA WITH DIALYTIKA AND TONOS
    0x00c1: 0x0391,	#  GREEK CAPITAL LETTER ALPHA
    0x00c2: 0x0392,	#  GREEK CAPITAL LETTER BETA
    0x00c3: 0x0393,	#  GREEK CAPITAL LETTER GAMMA
    0x00c4: 0x0394,	#  GREEK CAPITAL LETTER DELTA
    0x00c5: 0x0395,	#  GREEK CAPITAL LETTER EPSILON
    0x00c6: 0x0396,	#  GREEK CAPITAL LETTER ZETA
    0x00c7: 0x0397,	#  GREEK CAPITAL LETTER ETA
    0x00c8: 0x0398,	#  GREEK CAPITAL LETTER THETA
    0x00c9: 0x0399,	#  GREEK CAPITAL LETTER IOTA
    0x00ca: 0x039a,	#  GREEK CAPITAL LETTER KAPPA
    0x00cb: 0x039b,	#  GREEK CAPITAL LETTER LAMDA
    0x00cc: 0x039c,	#  GREEK CAPITAL LETTER MU
    0x00cd: 0x039d,	#  GREEK CAPITAL LETTER NU
    0x00ce: 0x039e,	#  GREEK CAPITAL LETTER XI
    0x00cf: 0x039f,	#  GREEK CAPITAL LETTER OMICRON
    0x00d0: 0x03a0,	#  GREEK CAPITAL LETTER PI
    0x00d1: 0x03a1,	#  GREEK CAPITAL LETTER RHO
    0x00d2: None,
    0x00d3: 0x03a3,	#  GREEK CAPITAL LETTER SIGMA
    0x00d4: 0x03a4,	#  GREEK CAPITAL LETTER TAU
    0x00d5: 0x03a5,	#  GREEK CAPITAL LETTER UPSILON
    0x00d6: 0x03a6,	#  GREEK CAPITAL LETTER PHI
    0x00d7: 0x03a7,	#  GREEK CAPITAL LETTER CHI
    0x00d8: 0x03a8,	#  GREEK CAPITAL LETTER PSI
    0x00d9: 0x03a9,	#  GREEK CAPITAL LETTER OMEGA
    0x00da: 0x03aa,	#  GREEK CAPITAL LETTER IOTA WITH DIALYTIKA
    0x00db: 0x03ab,	#  GREEK CAPITAL LETTER UPSILON WITH DIALYTIKA
    0x00dc: 0x03ac,	#  GREEK SMALL LETTER ALPHA WITH TONOS
    0x00dd: 0x03ad,	#  GREEK SMALL LETTER EPSILON WITH TONOS
    0x00de: 0x03ae,	#  GREEK SMALL LETTER ETA WITH TONOS
    0x00df: 0x03af,	#  GREEK SMALL LETTER IOTA WITH TONOS
    0x00e0: 0x03b0,	#  GREEK SMALL LETTER UPSILON WITH DIALYTIKA AND TONOS
    0x00e1: 0x03b1,	#  GREEK SMALL LETTER ALPHA
    0x00e2: 0x03b2,	#  GREEK SMALL LETTER BETA
    0x00e3: 0x03b3,	#  GREEK SMALL LETTER GAMMA
    0x00e4: 0x03b4,	#  GREEK SMALL LETTER DELTA
    0x00e5: 0x03b5,	#  GREEK SMALL LETTER EPSILON
    0x00e6: 0x03b6,	#  GREEK SMALL LETTER ZETA
    0x00e7: 0x03b7,	#  GREEK SMALL LETTER ETA
    0x00e8: 0x03b8,	#  GREEK SMALL LETTER THETA
    0x00e9: 0x03b9,	#  GREEK SMALL LETTER IOTA
    0x00ea: 0x03ba,	#  GREEK SMALL LETTER KAPPA
    0x00eb: 0x03bb,	#  GREEK SMALL LETTER LAMDA
    0x00ec: 0x03bc,	#  GREEK SMALL LETTER MU
    0x00ed: 0x03bd,	#  GREEK SMALL LETTER NU
    0x00ee: 0x03be,	#  GREEK SMALL LETTER XI
    0x00ef: 0x03bf,	#  GREEK SMALL LETTER OMICRON
    0x00f0: 0x03c0,	#  GREEK SMALL LETTER PI
    0x00f1: 0x03c1,	#  GREEK SMALL LETTER RHO
    0x00f2: 0x03c2,	#  GREEK SMALL LETTER FINAL SIGMA
    0x00f3: 0x03c3,	#  GREEK SMALL LETTER SIGMA
    0x00f4: 0x03c4,	#  GREEK SMALL LETTER TAU
    0x00f5: 0x03c5,	#  GREEK SMALL LETTER UPSILON
    0x00f6: 0x03c6,	#  GREEK SMALL LETTER PHI
    0x00f7: 0x03c7,	#  GREEK SMALL LETTER CHI
    0x00f8: 0x03c8,	#  GREEK SMALL LETTER PSI
    0x00f9: 0x03c9,	#  GREEK SMALL LETTER OMEGA
    0x00fa: 0x03ca,	#  GREEK SMALL LETTER IOTA WITH DIALYTIKA
    0x00fb: 0x03cb,	#  GREEK SMALL LETTER UPSILON WITH DIALYTIKA
    0x00fc: 0x03cc,	#  GREEK SMALL LETTER OMICRON WITH TONOS
    0x00fd: 0x03cd,	#  GREEK SMALL LETTER UPSILON WITH TONOS
    0x00fe: 0x03ce,	#  GREEK SMALL LETTER OMEGA WITH TONOS
    0x00ff: None,
})

### Decoding Table

decoding_table = (
    u'\x00'	#  0x0000 -> NULL
    u'\x01'	#  0x0001 -> START OF HEADING
    u'\x02'	#  0x0002 -> START OF TEXT
    u'\x03'	#  0x0003 -> END OF TEXT
    u'\x04'	#  0x0004 -> END OF TRANSMISSION
    u'\x05'	#  0x0005 -> ENQUIRY
    u'\x06'	#  0x0006 -> ACKNOWLEDGE
    u'\x07'	#  0x0007 -> BELL
    u'\x08'	#  0x0008 -> BACKSPACE
    u'\t'	#  0x0009 -> HORIZONTAL TABULATION
    u'\n'	#  0x000a -> LINE FEED
    u'\x0b'	#  0x000b -> VERTICAL TABULATION
    u'\x0c'	#  0x000c -> FORM FEED
    u'\r'	#  0x000d -> CARRIAGE RETURN
    u'\x0e'	#  0x000e -> SHIFT OUT
    u'\x0f'	#  0x000f -> SHIFT IN
    u'\x10'	#  0x0010 -> DATA LINK ESCAPE
    u'\x11'	#  0x0011 -> DEVICE CONTROL ONE
    u'\x12'	#  0x0012 -> DEVICE CONTROL TWO
    u'\x13'	#  0x0013 -> DEVICE CONTROL THREE
    u'\x14'	#  0x0014 -> DEVICE CONTROL FOUR
    u'\x15'	#  0x0015 -> NEGATIVE ACKNOWLEDGE
    u'\x16'	#  0x0016 -> SYNCHRONOUS IDLE
    u'\x17'	#  0x0017 -> END OF TRANSMISSION BLOCK
    u'\x18'	#  0x0018 -> CANCEL
    u'\x19'	#  0x0019 -> END OF MEDIUM
    u'\x1a'	#  0x001a -> SUBSTITUTE
    u'\x1b'	#  0x001b -> ESCAPE
    u'\x1c'	#  0x001c -> FILE SEPARATOR
    u'\x1d'	#  0x001d -> GROUP SEPARATOR
    u'\x1e'	#  0x001e -> RECORD SEPARATOR
    u'\x1f'	#  0x001f -> UNIT SEPARATOR
    u' '	#  0x0020 -> SPACE
    u'!'	#  0x0021 -> EXCLAMATION MARK
    u'"'	#  0x0022 -> QUOTATION MARK
    u'#'	#  0x0023 -> NUMBER SIGN
    u'$'	#  0x0024 -> DOLLAR SIGN
    u'%'	#  0x0025 -> PERCENT SIGN
    u'&'	#  0x0026 -> AMPERSAND
    u"'"	#  0x0027 -> APOSTROPHE
    u'('	#  0x0028 -> LEFT PARENTHESIS
    u')'	#  0x0029 -> RIGHT PARENTHESIS
    u'*'	#  0x002a -> ASTERISK
    u'+'	#  0x002b -> PLUS SIGN
    u','	#  0x002c -> COMMA
    u'-'	#  0x002d -> HYPHEN-MINUS
    u'.'	#  0x002e -> FULL STOP
    u'/'	#  0x002f -> SOLIDUS
    u'0'	#  0x0030 -> DIGIT ZERO
    u'1'	#  0x0031 -> DIGIT ONE
    u'2'	#  0x0032 -> DIGIT TWO
    u'3'	#  0x0033 -> DIGIT THREE
    u'4'	#  0x0034 -> DIGIT FOUR
    u'5'	#  0x0035 -> DIGIT FIVE
    u'6'	#  0x0036 -> DIGIT SIX
    u'7'	#  0x0037 -> DIGIT SEVEN
    u'8'	#  0x0038 -> DIGIT EIGHT
    u'9'	#  0x0039 -> DIGIT NINE
    u':'	#  0x003a -> COLON
    u';'	#  0x003b -> SEMICOLON
    u'<'	#  0x003c -> LESS-THAN SIGN
    u'='	#  0x003d -> EQUALS SIGN
    u'>'	#  0x003e -> GREATER-THAN SIGN
    u'?'	#  0x003f -> QUESTION MARK
    u'@'	#  0x0040 -> COMMERCIAL AT
    u'A'	#  0x0041 -> LATIN CAPITAL LETTER A
    u'B'	#  0x0042 -> LATIN CAPITAL LETTER B
    u'C'	#  0x0043 -> LATIN CAPITAL LETTER C
    u'D'	#  0x0044 -> LATIN CAPITAL LETTER D
    u'E'	#  0x0045 -> LATIN CAPITAL LETTER E
    u'F'	#  0x0046 -> LATIN CAPITAL LETTER F
    u'G'	#  0x0047 -> LATIN CAPITAL LETTER G
    u'H'	#  0x0048 -> LATIN CAPITAL LETTER H
    u'I'	#  0x0049 -> LATIN CAPITAL LETTER I
    u'J'	#  0x004a -> LATIN CAPITAL LETTER J
    u'K'	#  0x004b -> LATIN CAPITAL LETTER K
    u'L'	#  0x004c -> LATIN CAPITAL LETTER L
    u'M'	#  0x004d -> LATIN CAPITAL LETTER M
    u'N'	#  0x004e -> LATIN CAPITAL LETTER N
    u'O'	#  0x004f -> LATIN CAPITAL LETTER O
    u'P'	#  0x0050 -> LATIN CAPITAL LETTER P
    u'Q'	#  0x0051 -> LATIN CAPITAL LETTER Q
    u'R'	#  0x0052 -> LATIN CAPITAL LETTER R
    u'S'	#  0x0053 -> LATIN CAPITAL LETTER S
    u'T'	#  0x0054 -> LATIN CAPITAL LETTER T
    u'U'	#  0x0055 -> LATIN CAPITAL LETTER U
    u'V'	#  0x0056 -> LATIN CAPITAL LETTER V
    u'W'	#  0x0057 -> LATIN CAPITAL LETTER W
    u'X'	#  0x0058 -> LATIN CAPITAL LETTER X
    u'Y'	#  0x0059 -> LATIN CAPITAL LETTER Y
    u'Z'	#  0x005a -> LATIN CAPITAL LETTER Z
    u'['	#  0x005b -> LEFT SQUARE BRACKET
    u'\\'	#  0x005c -> REVERSE SOLIDUS
    u']'	#  0x005d -> RIGHT SQUARE BRACKET
    u'^'	#  0x005e -> CIRCUMFLEX ACCENT
    u'_'	#  0x005f -> LOW LINE
    u'`'	#  0x0060 -> GRAVE ACCENT
    u'a'	#  0x0061 -> LATIN SMALL LETTER A
    u'b'	#  0x0062 -> LATIN SMALL LETTER B
    u'c'	#  0x0063 -> LATIN SMALL LETTER C
    u'd'	#  0x0064 -> LATIN SMALL LETTER D
    u'e'	#  0x0065 -> LATIN SMALL LETTER E
    u'f'	#  0x0066 -> LATIN SMALL LETTER F
    u'g'	#  0x0067 -> LATIN SMALL LETTER G
    u'h'	#  0x0068 -> LATIN SMALL LETTER H
    u'i'	#  0x0069 -> LATIN SMALL LETTER I
    u'j'	#  0x006a -> LATIN SMALL LETTER J
    u'k'	#  0x006b -> LATIN SMALL LETTER K
    u'l'	#  0x006c -> LATIN SMALL LETTER L
    u'm'	#  0x006d -> LATIN SMALL LETTER M
    u'n'	#  0x006e -> LATIN SMALL LETTER N
    u'o'	#  0x006f -> LATIN SMALL LETTER O
    u'p'	#  0x0070 -> LATIN SMALL LETTER P
    u'q'	#  0x0071 -> LATIN SMALL LETTER Q
    u'r'	#  0x0072 -> LATIN SMALL LETTER R
    u's'	#  0x0073 -> LATIN SMALL LETTER S
    u't'	#  0x0074 -> LATIN SMALL LETTER T
    u'u'	#  0x0075 -> LATIN SMALL LETTER U
    u'v'	#  0x0076 -> LATIN SMALL LETTER V
    u'w'	#  0x0077 -> LATIN SMALL LETTER W
    u'x'	#  0x0078 -> LATIN SMALL LETTER X
    u'y'	#  0x0079 -> LATIN SMALL LETTER Y
    u'z'	#  0x007a -> LATIN SMALL LETTER Z
    u'{'	#  0x007b -> LEFT CURLY BRACKET
    u'|'	#  0x007c -> VERTICAL LINE
    u'}'	#  0x007d -> RIGHT CURLY BRACKET
    u'~'	#  0x007e -> TILDE
    u'\x7f'	#  0x007f -> DELETE
    u'\x80'	#  0x0080 -> <control>
    u'\x81'	#  0x0081 -> <control>
    u'\x82'	#  0x0082 -> <control>
    u'\x83'	#  0x0083 -> <control>
    u'\x84'	#  0x0084 -> <control>
    u'\x85'	#  0x0085 -> <control>
    u'\x86'	#  0x0086 -> <control>
    u'\x87'	#  0x0087 -> <control>
    u'\x88'	#  0x0088 -> <control>
    u'\x89'	#  0x0089 -> <control>
    u'\x8a'	#  0x008a -> <control>
    u'\x8b'	#  0x008b -> <control>
    u'\x8c'	#  0x008c -> <control>
    u'\x8d'	#  0x008d -> <control>
    u'\x8e'	#  0x008e -> <control>
    u'\x8f'	#  0x008f -> <control>
    u'\x90'	#  0x0090 -> <control>
    u'\x91'	#  0x0091 -> <control>
    u'\x92'	#  0x0092 -> <control>
    u'\x93'	#  0x0093 -> <control>
    u'\x94'	#  0x0094 -> <control>
    u'\x95'	#  0x0095 -> <control>
    u'\x96'	#  0x0096 -> <control>
    u'\x97'	#  0x0097 -> <control>
    u'\x98'	#  0x0098 -> <control>
    u'\x99'	#  0x0099 -> <control>
    u'\x9a'	#  0x009a -> <control>
    u'\x9b'	#  0x009b -> <control>
    u'\x9c'	#  0x009c -> <control>
    u'\x9d'	#  0x009d -> <control>
    u'\x9e'	#  0x009e -> <control>
    u'\x9f'	#  0x009f -> <control>
    u'\xa0'	#  0x00a0 -> NO-BREAK SPACE
    u'\u2018'	#  0x00a1 -> LEFT SINGLE QUOTATION MARK
    u'\u2019'	#  0x00a2 -> RIGHT SINGLE QUOTATION MARK
    u'\xa3'	#  0x00a3 -> POUND SIGN
    u'\u20ac'	#  0x00a4 -> EURO SIGN
    u'\u20af'	#  0x00a5 -> DRACHMA SIGN
    u'\xa6'	#  0x00a6 -> BROKEN BAR
    u'\xa7'	#  0x00a7 -> SECTION SIGN
    u'\xa8'	#  0x00a8 -> DIAERESIS
    u'\xa9'	#  0x00a9 -> COPYRIGHT SIGN
    u'\u037a'	#  0x00aa -> GREEK YPOGEGRAMMENI
    u'\xab'	#  0x00ab -> LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
    u'\xac'	#  0x00ac -> NOT SIGN
    u'\xad'	#  0x00ad -> SOFT HYPHEN
    u'\ufffe'
    u'\u2015'	#  0x00af -> HORIZONTAL BAR
    u'\xb0'	#  0x00b0 -> DEGREE SIGN
    u'\xb1'	#  0x00b1 -> PLUS-MINUS SIGN
    u'\xb2'	#  0x00b2 -> SUPERSCRIPT TWO
    u'\xb3'	#  0x00b3 -> SUPERSCRIPT THREE
    u'\u0384'	#  0x00b4 -> GREEK TONOS
    u'\u0385'	#  0x00b5 -> GREEK DIALYTIKA TONOS
    u'\u0386'	#  0x00b6 -> GREEK CAPITAL LETTER ALPHA WITH TONOS
    u'\xb7'	#  0x00b7 -> MIDDLE DOT
    u'\u0388'	#  0x00b8 -> GREEK CAPITAL LETTER EPSILON WITH TONOS
    u'\u0389'	#  0x00b9 -> GREEK CAPITAL LETTER ETA WITH TONOS
    u'\u038a'	#  0x00ba -> GREEK CAPITAL LETTER IOTA WITH TONOS
    u'\xbb'	#  0x00bb -> RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
    u'\u038c'	#  0x00bc -> GREEK CAPITAL LETTER OMICRON WITH TONOS
    u'\xbd'	#  0x00bd -> VULGAR FRACTION ONE HALF
    u'\u038e'	#  0x00be -> GREEK CAPITAL LETTER UPSILON WITH TONOS
    u'\u038f'	#  0x00bf -> GREEK CAPITAL LETTER OMEGA WITH TONOS
    u'\u0390'	#  0x00c0 -> GREEK SMALL LETTER IOTA WITH DIALYTIKA AND TONOS
    u'\u0391'	#  0x00c1 -> GREEK CAPITAL LETTER ALPHA
    u'\u0392'	#  0x00c2 -> GREEK CAPITAL LETTER BETA
    u'\u0393'	#  0x00c3 -> GREEK CAPITAL LETTER GAMMA
    u'\u0394'	#  0x00c4 -> GREEK CAPITAL LETTER DELTA
    u'\u0395'	#  0x00c5 -> GREEK CAPITAL LETTER EPSILON
    u'\u0396'	#  0x00c6 -> GREEK CAPITAL LETTER ZETA
    u'\u0397'	#  0x00c7 -> GREEK CAPITAL LETTER ETA
    u'\u0398'	#  0x00c8 -> GREEK CAPITAL LETTER THETA
    u'\u0399'	#  0x00c9 -> GREEK CAPITAL LETTER IOTA
    u'\u039a'	#  0x00ca -> GREEK CAPITAL LETTER KAPPA
    u'\u039b'	#  0x00cb -> GREEK CAPITAL LETTER LAMDA
    u'\u039c'	#  0x00cc -> GREEK CAPITAL LETTER MU
    u'\u039d'	#  0x00cd -> GREEK CAPITAL LETTER NU
    u'\u039e'	#  0x00ce -> GREEK CAPITAL LETTER XI
    u'\u039f'	#  0x00cf -> GREEK CAPITAL LETTER OMICRON
    u'\u03a0'	#  0x00d0 -> GREEK CAPITAL LETTER PI
    u'\u03a1'	#  0x00d1 -> GREEK CAPITAL LETTER RHO
    u'\ufffe'
    u'\u03a3'	#  0x00d3 -> GREEK CAPITAL LETTER SIGMA
    u'\u03a4'	#  0x00d4 -> GREEK CAPITAL LETTER TAU
    u'\u03a5'	#  0x00d5 -> GREEK CAPITAL LETTER UPSILON
    u'\u03a6'	#  0x00d6 -> GREEK CAPITAL LETTER PHI
    u'\u03a7'	#  0x00d7 -> GREEK CAPITAL LETTER CHI
    u'\u03a8'	#  0x00d8 -> GREEK CAPITAL LETTER PSI
    u'\u03a9'	#  0x00d9 -> GREEK CAPITAL LETTER OMEGA
    u'\u03aa'	#  0x00da -> GREEK CAPITAL LETTER IOTA WITH DIALYTIKA
    u'\u03ab'	#  0x00db -> GREEK CAPITAL LETTER UPSILON WITH DIALYTIKA
    u'\u03ac'	#  0x00dc -> GREEK SMALL LETTER ALPHA WITH TONOS
    u'\u03ad'	#  0x00dd -> GREEK SMALL LETTER EPSILON WITH TONOS
    u'\u03ae'	#  0x00de -> GREEK SMALL LETTER ETA WITH TONOS
    u'\u03af'	#  0x00df -> GREEK SMALL LETTER IOTA WITH TONOS
    u'\u03b0'	#  0x00e0 -> GREEK SMALL LETTER UPSILON WITH DIALYTIKA AND TONOS
    u'\u03b1'	#  0x00e1 -> GREEK SMALL LETTER ALPHA
    u'\u03b2'	#  0x00e2 -> GREEK SMALL LETTER BETA
    u'\u03b3'	#  0x00e3 -> GREEK SMALL LETTER GAMMA
    u'\u03b4'	#  0x00e4 -> GREEK SMALL LETTER DELTA
    u'\u03b5'	#  0x00e5 -> GREEK SMALL LETTER EPSILON
    u'\u03b6'	#  0x00e6 -> GREEK SMALL LETTER ZETA
    u'\u03b7'	#  0x00e7 -> GREEK SMALL LETTER ETA
    u'\u03b8'	#  0x00e8 -> GREEK SMALL LETTER THETA
    u'\u03b9'	#  0x00e9 -> GREEK SMALL LETTER IOTA
    u'\u03ba'	#  0x00ea -> GREEK SMALL LETTER KAPPA
    u'\u03bb'	#  0x00eb -> GREEK SMALL LETTER LAMDA
    u'\u03bc'	#  0x00ec -> GREEK SMALL LETTER MU
    u'\u03bd'	#  0x00ed -> GREEK SMALL LETTER NU
    u'\u03be'	#  0x00ee -> GREEK SMALL LETTER XI
    u'\u03bf'	#  0x00ef -> GREEK SMALL LETTER OMICRON
    u'\u03c0'	#  0x00f0 -> GREEK SMALL LETTER PI
    u'\u03c1'	#  0x00f1 -> GREEK SMALL LETTER RHO
    u'\u03c2'	#  0x00f2 -> GREEK SMALL LETTER FINAL SIGMA
    u'\u03c3'	#  0x00f3 -> GREEK SMALL LETTER SIGMA
    u'\u03c4'	#  0x00f4 -> GREEK SMALL LETTER TAU
    u'\u03c5'	#  0x00f5 -> GREEK SMALL LETTER UPSILON
    u'\u03c6'	#  0x00f6 -> GREEK SMALL LETTER PHI
    u'\u03c7'	#  0x00f7 -> GREEK SMALL LETTER CHI
    u'\u03c8'	#  0x00f8 -> GREEK SMALL LETTER PSI
    u'\u03c9'	#  0x00f9 -> GREEK SMALL LETTER OMEGA
    u'\u03ca'	#  0x00fa -> GREEK SMALL LETTER IOTA WITH DIALYTIKA
    u'\u03cb'	#  0x00fb -> GREEK SMALL LETTER UPSILON WITH DIALYTIKA
    u'\u03cc'	#  0x00fc -> GREEK SMALL LETTER OMICRON WITH TONOS
    u'\u03cd'	#  0x00fd -> GREEK SMALL LETTER UPSILON WITH TONOS
    u'\u03ce'	#  0x00fe -> GREEK SMALL LETTER OMEGA WITH TONOS
    u'\ufffe'
)

### Encoding Map

encoding_map = {
    0x0000: 0x0000,	#  NULL
    0x0001: 0x0001,	#  START OF HEADING
    0x0002: 0x0002,	#  START OF TEXT
    0x0003: 0x0003,	#  END OF TEXT
    0x0004: 0x0004,	#  END OF TRANSMISSION
    0x0005: 0x0005,	#  ENQUIRY
    0x0006: 0x0006,	#  ACKNOWLEDGE
    0x0007: 0x0007,	#  BELL
    0x0008: 0x0008,	#  BACKSPACE
    0x0009: 0x0009,	#  HORIZONTAL TABULATION
    0x000a: 0x000a,	#  LINE FEED
    0x000b: 0x000b,	#  VERTICAL TABULATION
    0x000c: 0x000c,	#  FORM FEED
    0x000d: 0x000d,	#  CARRIAGE RETURN
    0x000e: 0x000e,	#  SHIFT OUT
    0x000f: 0x000f,	#  SHIFT IN
    0x0010: 0x0010,	#  DATA LINK ESCAPE
    0x0011: 0x0011,	#  DEVICE CONTROL ONE
    0x0012: 0x0012,	#  DEVICE CONTROL TWO
    0x0013: 0x0013,	#  DEVICE CONTROL THREE
    0x0014: 0x0014,	#  DEVICE CONTROL FOUR
    0x0015: 0x0015,	#  NEGATIVE ACKNOWLEDGE
    0x0016: 0x0016,	#  SYNCHRONOUS IDLE
    0x0017: 0x0017,	#  END OF TRANSMISSION BLOCK
    0x0018: 0x0018,	#  CANCEL
    0x0019: 0x0019,	#  END OF MEDIUM
    0x001a: 0x001a,	#  SUBSTITUTE
    0x001b: 0x001b,	#  ESCAPE
    0x001c: 0x001c,	#  FILE SEPARATOR
    0x001d: 0x001d,	#  GROUP SEPARATOR
    0x001e: 0x001e,	#  RECORD SEPARATOR
    0x001f: 0x001f,	#  UNIT SEPARATOR
    0x0020: 0x0020,	#  SPACE
    0x0021: 0x0021,	#  EXCLAMATION MARK
    0x0022: 0x0022,	#  QUOTATION MARK
    0x0023: 0x0023,	#  NUMBER SIGN
    0x0024: 0x0024,	#  DOLLAR SIGN
    0x0025: 0x0025,	#  PERCENT SIGN
    0x0026: 0x0026,	#  AMPERSAND
    0x0027: 0x0027,	#  APOSTROPHE
    0x0028: 0x0028,	#  LEFT PARENTHESIS
    0x0029: 0x0029,	#  RIGHT PARENTHESIS
    0x002a: 0x002a,	#  ASTERISK
    0x002b: 0x002b,	#  PLUS SIGN
    0x002c: 0x002c,	#  COMMA
    0x002d: 0x002d,	#  HYPHEN-MINUS
    0x002e: 0x002e,	#  FULL STOP
    0x002f: 0x002f,	#  SOLIDUS
    0x0030: 0x0030,	#  DIGIT ZERO
    0x0031: 0x0031,	#  DIGIT ONE
    0x0032: 0x0032,	#  DIGIT TWO
    0x0033: 0x0033,	#  DIGIT THREE
    0x0034: 0x0034,	#  DIGIT FOUR
    0x0035: 0x0035,	#  DIGIT FIVE
    0x0036: 0x0036,	#  DIGIT SIX
    0x0037: 0x0037,	#  DIGIT SEVEN
    0x0038: 0x0038,	#  DIGIT EIGHT
    0x0039: 0x0039,	#  DIGIT NINE
    0x003a: 0x003a,	#  COLON
    0x003b: 0x003b,	#  SEMICOLON
    0x003c: 0x003c,	#  LESS-THAN SIGN
    0x003d: 0x003d,	#  EQUALS SIGN
    0x003e: 0x003e,	#  GREATER-THAN SIGN
    0x003f: 0x003f,	#  QUESTION MARK
    0x0040: 0x0040,	#  COMMERCIAL AT
    0x0041: 0x0041,	#  LATIN CAPITAL LETTER A
    0x0042: 0x0042,	#  LATIN CAPITAL LETTER B
    0x0043: 0x0043,	#  LATIN CAPITAL LETTER C
    0x0044: 0x0044,	#  LATIN CAPITAL LETTER D
    0x0045: 0x0045,	#  LATIN CAPITAL LETTER E
    0x0046: 0x0046,	#  LATIN CAPITAL LETTER F
    0x0047: 0x0047,	#  LATIN CAPITAL LETTER G
    0x0048: 0x0048,	#  LATIN CAPITAL LETTER H
    0x0049: 0x0049,	#  LATIN CAPITAL LETTER I
    0x004a: 0x004a,	#  LATIN CAPITAL LETTER J
    0x004b: 0x004b,	#  LATIN CAPITAL LETTER K
    0x004c: 0x004c,	#  LATIN CAPITAL LETTER L
    0x004d: 0x004d,	#  LATIN CAPITAL LETTER M
    0x004e: 0x004e,	#  LATIN CAPITAL LETTER N
    0x004f: 0x004f,	#  LATIN CAPITAL LETTER O
    0x0050: 0x0050,	#  LATIN CAPITAL LETTER P
    0x0051: 0x0051,	#  LATIN CAPITAL LETTER Q
    0x0052: 0x0052,	#  LATIN CAPITAL LETTER R
    0x0053: 0x0053,	#  LATIN CAPITAL LETTER S
    0x0054: 0x0054,	#  LATIN CAPITAL LETTER T
    0x0055: 0x0055,	#  LATIN CAPITAL LETTER U
    0x0056: 0x0056,	#  LATIN CAPITAL LETTER V
    0x0057: 0x0057,	#  LATIN CAPITAL LETTER W
    0x0058: 0x0058,	#  LATIN CAPITAL LETTER X
    0x0059: 0x0059,	#  LATIN CAPITAL LETTER Y
    0x005a: 0x005a,	#  LATIN CAPITAL LETTER Z
    0x005b: 0x005b,	#  LEFT SQUARE BRACKET
    0x005c: 0x005c,	#  REVERSE SOLIDUS
    0x005d: 0x005d,	#  RIGHT SQUARE BRACKET
    0x005e: 0x005e,	#  CIRCUMFLEX ACCENT
    0x005f: 0x005f,	#  LOW LINE
    0x0060: 0x0060,	#  GRAVE ACCENT
    0x0061: 0x0061,	#  LATIN SMALL LETTER A
    0x0062: 0x0062,	#  LATIN SMALL LETTER B
    0x0063: 0x0063,	#  LATIN SMALL LETTER C
    0x0064: 0x0064,	#  LATIN SMALL LETTER D
    0x0065: 0x0065,	#  LATIN SMALL LETTER E
    0x0066: 0x0066,	#  LATIN SMALL LETTER F
    0x0067: 0x0067,	#  LATIN SMALL LETTER G
    0x0068: 0x0068,	#  LATIN SMALL LETTER H
    0x0069: 0x0069,	#  LATIN SMALL LETTER I
    0x006a: 0x006a,	#  LATIN SMALL LETTER J
    0x006b: 0x006b,	#  LATIN SMALL LETTER K
    0x006c: 0x006c,	#  LATIN SMALL LETTER L
    0x006d: 0x006d,	#  LATIN SMALL LETTER M
    0x006e: 0x006e,	#  LATIN SMALL LETTER N
    0x006f: 0x006f,	#  LATIN SMALL LETTER O
    0x0070: 0x0070,	#  LATIN SMALL LETTER P
    0x0071: 0x0071,	#  LATIN SMALL LETTER Q
    0x0072: 0x0072,	#  LATIN SMALL LETTER R
    0x0073: 0x0073,	#  LATIN SMALL LETTER S
    0x0074: 0x0074,	#  LATIN SMALL LETTER T
    0x0075: 0x0075,	#  LATIN SMALL LETTER U
    0x0076: 0x0076,	#  LATIN SMALL LETTER V
    0x0077: 0x0077,	#  LATIN SMALL LETTER W
    0x0078: 0x0078,	#  LATIN SMALL LETTER X
    0x0079: 0x0079,	#  LATIN SMALL LETTER Y
    0x007a: 0x007a,	#  LATIN SMALL LETTER Z
    0x007b: 0x007b,	#  LEFT CURLY BRACKET
    0x007c: 0x007c,	#  VERTICAL LINE
    0x007d: 0x007d,	#  RIGHT CURLY BRACKET
    0x007e: 0x007e,	#  TILDE
    0x007f: 0x007f,	#  DELETE
    0x0080: 0x0080,	#  <control>
    0x0081: 0x0081,	#  <control>
    0x0082: 0x0082,	#  <control>
    0x0083: 0x0083,	#  <control>
    0x0084: 0x0084,	#  <control>
    0x0085: 0x0085,	#  <control>
    0x0086: 0x0086,	#  <control>
    0x0087: 0x0087,	#  <control>
    0x0088: 0x0088,	#  <control>
    0x0089: 0x0089,	#  <control>
    0x008a: 0x008a,	#  <control>
    0x008b: 0x008b,	#  <control>
    0x008c: 0x008c,	#  <control>
    0x008d: 0x008d,	#  <control>
    0x008e: 0x008e,	#  <control>
    0x008f: 0x008f,	#  <control>
    0x0090: 0x0090,	#  <control>
    0x0091: 0x0091,	#  <control>
    0x0092: 0x0092,	#  <control>
    0x0093: 0x0093,	#  <control>
    0x0094: 0x0094,	#  <control>
    0x0095: 0x0095,	#  <control>
    0x0096: 0x0096,	#  <control>
    0x0097: 0x0097,	#  <control>
    0x0098: 0x0098,	#  <control>
    0x0099: 0x0099,	#  <control>
    0x009a: 0x009a,	#  <control>
    0x009b: 0x009b,	#  <control>
    0x009c: 0x009c,	#  <control>
    0x009d: 0x009d,	#  <control>
    0x009e: 0x009e,	#  <control>
    0x009f: 0x009f,	#  <control>
    0x00a0: 0x00a0,	#  NO-BREAK SPACE
    0x00a3: 0x00a3,	#  POUND SIGN
    0x00a6: 0x00a6,	#  BROKEN BAR
    0x00a7: 0x00a7,	#  SECTION SIGN
    0x00a8: 0x00a8,	#  DIAERESIS
    0x00a9: 0x00a9,	#  COPYRIGHT SIGN
    0x00ab: 0x00ab,	#  LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
    0x00ac: 0x00ac,	#  NOT SIGN
    0x00ad: 0x00ad,	#  SOFT HYPHEN
    0x00b0: 0x00b0,	#  DEGREE SIGN
    0x00b1: 0x00b1,	#  PLUS-MINUS SIGN
    0x00b2: 0x00b2,	#  SUPERSCRIPT TWO
    0x00b3: 0x00b3,	#  SUPERSCRIPT THREE
    0x00b7: 0x00b7,	#  MIDDLE DOT
    0x00bb: 0x00bb,	#  RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
    0x00bd: 0x00bd,	#  VULGAR FRACTION ONE HALF
    0x037a: 0x00aa,	#  GREEK YPOGEGRAMMENI
    0x0384: 0x00b4,	#  GREEK TONOS
    0x0385: 0x00b5,	#  GREEK DIALYTIKA TONOS
    0x0386: 0x00b6,	#  GREEK CAPITAL LETTER ALPHA WITH TONOS
    0x0388: 0x00b8,	#  GREEK CAPITAL LETTER EPSILON WITH TONOS
    0x0389: 0x00b9,	#  GREEK CAPITAL LETTER ETA WITH TONOS
    0x038a: 0x00ba,	#  GREEK CAPITAL LETTER IOTA WITH TONOS
    0x038c: 0x00bc,	#  GREEK CAPITAL LETTER OMICRON WITH TONOS
    0x038e: 0x00be,	#  GREEK CAPITAL LETTER UPSILON WITH TONOS
    0x038f: 0x00bf,	#  GREEK CAPITAL LETTER OMEGA WITH TONOS
    0x0390: 0x00c0,	#  GREEK SMALL LETTER IOTA WITH DIALYTIKA AND TONOS
    0x0391: 0x00c1,	#  GREEK CAPITAL LETTER ALPHA
    0x0392: 0x00c2,	#  GREEK CAPITAL LETTER BETA
    0x0393: 0x00c3,	#  GREEK CAPITAL LETTER GAMMA
    0x0394: 0x00c4,	#  GREEK CAPITAL LETTER DELTA
    0x0395: 0x00c5,	#  GREEK CAPITAL LETTER EPSILON
    0x0396: 0x00c6,	#  GREEK CAPITAL LETTER ZETA
    0x0397: 0x00c7,	#  GREEK CAPITAL LETTER ETA
    0x0398: 0x00c8,	#  GREEK CAPITAL LETTER THETA
    0x0399: 0x00c9,	#  GREEK CAPITAL LETTER IOTA
    0x039a: 0x00ca,	#  GREEK CAPITAL LETTER KAPPA
    0x039b: 0x00cb,	#  GREEK CAPITAL LETTER LAMDA
    0x039c: 0x00cc,	#  GREEK CAPITAL LETTER MU
    0x039d: 0x00cd,	#  GREEK CAPITAL LETTER NU
    0x039e: 0x00ce,	#  GREEK CAPITAL LETTER XI
    0x039f: 0x00cf,	#  GREEK CAPITAL LETTER OMICRON
    0x03a0: 0x00d0,	#  GREEK CAPITAL LETTER PI
    0x03a1: 0x00d1,	#  GREEK CAPITAL LETTER RHO
    0x03a3: 0x00d3,	#  GREEK CAPITAL LETTER SIGMA
    0x03a4: 0x00d4,	#  GREEK CAPITAL LETTER TAU
    0x03a5: 0x00d5,	#  GREEK CAPITAL LETTER UPSILON
    0x03a6: 0x00d6,	#  GREEK CAPITAL LETTER PHI
    0x03a7: 0x00d7,	#  GREEK CAPITAL LETTER CHI
    0x03a8: 0x00d8,	#  GREEK CAPITAL LETTER PSI
    0x03a9: 0x00d9,	#  GREEK CAPITAL LETTER OMEGA
    0x03aa: 0x00da,	#  GREEK CAPITAL LETTER IOTA WITH DIALYTIKA
    0x03ab: 0x00db,	#  GREEK CAPITAL LETTER UPSILON WITH DIALYTIKA
    0x03ac: 0x00dc,	#  GREEK SMALL LETTER ALPHA WITH TONOS
    0x03ad: 0x00dd,	#  GREEK SMALL LETTER EPSILON WITH TONOS
    0x03ae: 0x00de,	#  GREEK SMALL LETTER ETA WITH TONOS
    0x03af: 0x00df,	#  GREEK SMALL LETTER IOTA WITH TONOS
    0x03b0: 0x00e0,	#  GREEK SMALL LETTER UPSILON WITH DIALYTIKA AND TONOS
    0x03b1: 0x00e1,	#  GREEK SMALL LETTER ALPHA
    0x03b2: 0x00e2,	#  GREEK SMALL LETTER BETA
    0x03b3: 0x00e3,	#  GREEK SMALL LETTER GAMMA
    0x03b4: 0x00e4,	#  GREEK SMALL LETTER DELTA
    0x03b5: 0x00e5,	#  GREEK SMALL LETTER EPSILON
    0x03b6: 0x00e6,	#  GREEK SMALL LETTER ZETA
    0x03b7: 0x00e7,	#  GREEK SMALL LETTER ETA
    0x03b8: 0x00e8,	#  GREEK SMALL LETTER THETA
    0x03b9: 0x00e9,	#  GREEK SMALL LETTER IOTA
    0x03ba: 0x00ea,	#  GREEK SMALL LETTER KAPPA
    0x03bb: 0x00eb,	#  GREEK SMALL LETTER LAMDA
    0x03bc: 0x00ec,	#  GREEK SMALL LETTER MU
    0x03bd: 0x00ed,	#  GREEK SMALL LETTER NU
    0x03be: 0x00ee,	#  GREEK SMALL LETTER XI
    0x03bf: 0x00ef,	#  GREEK SMALL LETTER OMICRON
    0x03c0: 0x00f0,	#  GREEK SMALL LETTER PI
    0x03c1: 0x00f1,	#  GREEK SMALL LETTER RHO
    0x03c2: 0x00f2,	#  GREEK SMALL LETTER FINAL SIGMA
    0x03c3: 0x00f3,	#  GREEK SMALL LETTER SIGMA
    0x03c4: 0x00f4,	#  GREEK SMALL LETTER TAU
    0x03c5: 0x00f5,	#  GREEK SMALL LETTER UPSILON
    0x03c6: 0x00f6,	#  GREEK SMALL LETTER PHI
    0x03c7: 0x00f7,	#  GREEK SMALL LETTER CHI
    0x03c8: 0x00f8,	#  GREEK SMALL LETTER PSI
    0x03c9: 0x00f9,	#  GREEK SMALL LETTER OMEGA
    0x03ca: 0x00fa,	#  GREEK SMALL LETTER IOTA WITH DIALYTIKA
    0x03cb: 0x00fb,	#  GREEK SMALL LETTER UPSILON WITH DIALYTIKA
    0x03cc: 0x00fc,	#  GREEK SMALL LETTER OMICRON WITH TONOS
    0x03cd: 0x00fd,	#  GREEK SMALL LETTER UPSILON WITH TONOS
    0x03ce: 0x00fe,	#  GREEK SMALL LETTER OMEGA WITH TONOS
    0x2015: 0x00af,	#  HORIZONTAL BAR
    0x2018: 0x00a1,	#  LEFT SINGLE QUOTATION MARK
    0x2019: 0x00a2,	#  RIGHT SINGLE QUOTATION MARK
    0x20ac: 0x00a4,	#  EURO SIGN
    0x20af: 0x00a5,	#  DRACHMA SIGN
}
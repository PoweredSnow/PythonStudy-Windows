# import base64


# str2 = "e3nifIH9b_C@n@dH"
# flag = ""
# for i in range(len(str2)):
#     flag += chr(ord(str2[i]) - i)
# print((base64.b64decode(flag)).decode())


# xor
# b = [0] * 33
# b = [0x66, 0x0A, 0x6B, 0x0C, 0x77, 0x26, 0x4F, 0x2E, 0x40, 0x11,
#      0x78, 0x0D, 0x5A, 0x3B, 0x55, 0x11, 0x70, 0x19, 0x46, 0x1F,
#      0x76, 0x22, 0x4D, 0x23, 0x44, 0x0E, 0x67, 0x06, 0x68, 0x0F,
#      0x47, 0x32, 0x4F]
# for i in range(0, 32):
#     b[i] ^= b[i + 1]
#     print(chr(b[i]), end='')


# ConsoleApplication4
# 0073E968 | .  68 F0B07E00   push ConsoleA.007EB0F0
# v3 = [0] * 56
# v2 = [0] * 56
# v3[0] = 18
# v3[1] = 64
# v3[2] = 98
# v3[3] = 5
# v3[4] = 2
# v3[5] = 4
# v3[6] = 6
# v3[7] = 3
# v3[8] = 6
# v3[9] = 48
# v3[10] = 49
# v3[11] = 65
# v3[12] = 32
# v3[13] = 12
# v3[14] = 48
# v3[15] = 65
# v3[16] = 31
# v3[17] = 78
# v3[18] = 62
# v3[19] = 32
# v3[20] = 49
# v3[21] = 32
# v3[22] = 1
# v3[23] = 57
# v3[24] = 96
# v3[25] = 3
# v3[26] = 21
# v3[27] = 9
# v3[28] = 4
# v3[29] = 62
# v3[30] = 3
# v3[31] = 5
# v3[32] = 4
# v3[33] = 1
# v3[34] = 2
# v3[35] = 3
# v3[36] = 44
# v3[37] = 65
# v3[38] = 78
# v3[39] = 32
# v3[40] = 16
# v3[41] = 97
# v3[42] = 54
# v3[43] = 16
# v3[44] = 44
# v3[45] = 52
# v3[46] = 32
# v3[47] = 64
# v3[48] = 89
# v3[49] = 45
# v3[50] = 32
# v3[51] = 65
# v3[52] = 15
# v3[53] = 34
# v3[54] = 18
# v3[55] = 16
# v2[0] = 123
# v2[1] = 32
# v2[2] = 18
# v2[3] = 98
# v2[4] = 119
# v2[5] = 108
# v2[6] = 65
# v2[7] = 41
# v2[8] = 124
# v2[9] = 80
# v2[10] = 125
# v2[11] = 38
# v2[12] = 124
# v2[13] = 111
# v2[14] = 74
# v2[15] = 49
# v2[16] = 83
# v2[17] = 108
# v2[18] = 94
# v2[19] = 108
# v2[20] = 84
# v2[21] = 6
# v5 = "`S,yhn _uec{"
# v2[34] = 127
# v2[35] = 119
# v2[36] = 96
# v2[37] = 48
# v2[38] = 107
# v2[39] = 71
# v2[40] = 92
# v2[41] = 29
# v2[42] = 81
# v2[43] = 107
# v2[44] = 90
# v2[45] = 85
# v2[46] = 64
# v2[47] = 12
# v2[48] = 43
# v2[49] = 76
# v2[50] = 86
# v2[51] = 13
# v2[52] = 114
# v2[53] = 1
# v2[54] = 117
# v2[55] = 126
# v6 = "u~"
# j = 22
# for i in v5:
#     v2[j] = ord(i)
#     # print(v2[j], end=' ')
#     j += 1
# k = 54
# for i in v6:
#     v2[k] = ord(i)
#     print(v2[j], end=' ')
#     j += 1
# for i in range(56):
#     v2[i] ^= v3[i]
#     v2[i] ^= 0x13
#     print(chr(v2[i]), end='')


# flag1 = '0tem0c1eW{FTCTUD'
# flag2 = '}FTCTUD'
# print(flag1[::-1] + flag2[::-1])

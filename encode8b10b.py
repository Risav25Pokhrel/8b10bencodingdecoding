
class EncodeDecode:
    lookup5b=['100111','011101','101101','110001','110101','101001','011001','111000','111001','100101','010101','110100','001101','101100','011100','010111','011011','100011','010011','110010','001011','101010','011010','111010','110011','100110','010110','110110','001110','101110','011110','101011']
    lookup3b=['1011','1001','0101','1100','1101','1010','0110','1110','0111','1011','0110','1010','1100','1101','0101','1001','0111']
    encodedList=[]
    toComplement5B=False
    toComplement3B=False
    __toDecimal=lambda self,binary_num: int(binary_num,2)


    def get_No_Of_One(self,byte):
        return byte.count('1')

    def get5BData(self,byte):
        i=self.__toDecimal(byte)
        encodingData=self.lookup5b[i]
        if self.get_No_Of_One(encodingData) == 4:
            return encodingData
        else:
            if self.toComplement5B:
                complemented_string = ''.join(['1' if bit == '0' else '0' for bit in encodingData])
                encodingData=complemented_string
        self.toComplement5B=self.get_No_Of_One(encodingData)>3
        return encodingData

    def get3BData(self,byte):
        i=self.__toDecimal(byte)
        encodingData=self.lookup3b[i]
        if self.get_No_Of_One(encodingData) == 2:
            return encodingData
        else:
            if self.toComplement3B:
                complemented_string = ''.join(['1' if bit == '0' else '0' for bit in encodingData])
                encodingData=complemented_string
        self.toComplement3B=self.get_No_Of_One(encodingData)>2
        return encodingData

    def encode(self,bytes:str):
        leftArg,rightArg=bytes[:5],bytes[5:]
        fiveB,threeB=self.get5BData(leftArg),self.get3BData(rightArg)
        byte=fiveB,threeB
        self.encodedList.append(byte)
        print(bytes, byte ,end="\n")

    def decode(self,bytes:str):
        return "implement garna baki"






def openFile(file_path):
    with open(file_path,'rb') as file:
        content=file.read()
        a=EncodeDecode()
        for byte in content:
            bin=format(byte,'08b')
            a.encode(bin)


filePath="C:\\Users\\USER\\Desktop\\minor\\8b\\pooja.jpg"
openFile(filePath)


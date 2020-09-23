class Restaurant:
    def __init__(self,re_name,cu_type):
        self.re_name=re_name
        self.cu_type=cu_type
    def descripe_restaurant(self):
        print("餐馆名字叫做%s"%self.re_name)
        print("餐馆类型为%s"%self.cu_type)
    def open_restaturant(self):
        print('The restaurant is opening')
res=Restaurant('传统小吃','小吃店')
res.__init__('传统小吃','小吃店')
res.descripe_restaurant()
res.open_restaturant()
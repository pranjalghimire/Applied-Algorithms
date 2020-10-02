
def helper(num):
    less_than_20 = ["", "One", "Two", "Three", "Four", "Five", "Six",
    "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
    "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",  "Nineteen"]
    tens = ["","Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty","Ninety"]
    thousands = ["", "Thousand", "Million", "Billion"]
    hundreds=["", "One-hundred", "Two-hundred", "Three-hundred", "Four-hundred", "Five-hundred", "Six-hundred",
    "Seven-hundred", "Eight-hundred", "Nine-hundred"]
    ans=""
    if num==0:
        return "Zero"

    while (num//1000000000)>0:
      ans+=less_than_20[num//1000000000]+ " "+"Billion"
      num=num%1000000000

    while num//100000000>0:
       ans+=hundreds[num//100000000]+ " "+"Million"
       num=num%100000000
    while num//10000000>0:
       ans+=less_than_20[num//1000000]+ " Million"
       num=num%10000000

    print(ans)
print(helper(150000000))

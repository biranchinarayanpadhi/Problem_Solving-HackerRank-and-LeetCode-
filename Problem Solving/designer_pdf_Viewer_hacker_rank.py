word="abcd"

h=[1,2,3,2]
def designerPdfViewer(h, word):
    li=[]
    for i in word:
        li.append(ord(i)-97)

    final=[]
    for i in range(len(li)):
        final.append(h[li[i]])

    print(max(final)*len(word))
    
designerPdfViewer(h,word)
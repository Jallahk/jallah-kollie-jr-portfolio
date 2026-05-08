window.PORTFOLIO_DATA = {
  "generated_at": "2026-05-08T00:31:10.932209",
  "generated_at_label": "May 08, 2026 12:31 AM",
  "latest_modified_label": "Dec 09, 2025",
  "sections": [
    {
      "name": "Machine Learning",
      "path": "/Users/jallahkollie/PycharmProjects/PythonMiniProject /Machine Learning",
      "available": true
    },
    {
      "name": "A&D",
      "path": "/Users/jallahkollie/PycharmProjects/A&D",
      "available": true
    },
    {
      "name": "BirdBrain",
      "path": "/Users/jallahkollie/PycharmProjects/BIrdBrain",
      "available": false
    }
  ],
  "section_counts": {
    "A&D": 30,
    "Machine Learning": 105
  },
  "files": [
    {
      "id": "a-d-anagrams-py",
      "title": "anagrams",
      "section": "A&D",
      "relative_path": "anagrams.py",
      "summary": "In this project, I focus on time complexity of functions that test for anagrams. I implement functions such as anagramSolution1, anagramSolution2, anagramSolution3, and anagramSolution4. I build reusable functions.",
      "line_count": 92,
      "size_label": "1.8 KB",
      "modified": "2025-08-28T11:48:00.846529",
      "modified_label": "Aug 28, 2025",
      "file_url": "files/a-d/anagrams.py",
      "preview": "\"\"\"Time complexity of functions that test for anagrams\"\"\"\n\n#Checking Off\ndef anagramSolution1(s1,s2):\n    alist = list(s2)\n\n    pos1 = 0\n    stillOK = True\n\n    while pos1 < len(s1) and stillOK:\n        pos2 = 0\n        found = False\n        while pos2 < len(alist) and not found:\n            if s1[pos1] == alist[pos2]:\n                found = True\n            else:\n                pos2 = pos2 + 1\n        \n        if found:\n            alist[pos2] = None",
      "tags": [
        "A&D",
        "Python"
      ]
    },
    {
      "id": "a-d-anagrams2-py",
      "title": "anagrams2",
      "section": "A&D",
      "relative_path": "anagrams2.py",
      "summary": "In this project, I focus on time complexity of functions that test for anagrams. I implement functions such as anagramSolution1, anagramSolution2, anagramSolution4, and makeBigStrings. I include randomized behavior. I build reusable functions.",
      "line_count": 100,
      "size_label": "2.0 KB",
      "modified": "2025-09-02T21:10:53.169036",
      "modified_label": "Sep 02, 2025",
      "file_url": "files/a-d/anagrams2.py",
      "preview": "\"\"\"Time complexity of functions that test for anagrams\"\"\"\n\n#Checking Off\ndef anagramSolution1(s1,s2):\n    alist = list(s2)\n\n    pos1 = 0\n    stillOK = True\n\n    while pos1 < len(s1) and stillOK:\n        pos2 = 0\n        found = False\n        while pos2 < len(alist) and not found:\n            if s1[pos1] == alist[pos2]:\n                found = True\n            else:\n                pos2 = pos2 + 1\n\n        if found:\n            alist[pos2] = None",
      "tags": [
        "A&D",
        "Python"
      ]
    },
    {
      "id": "a-d-baseconverter-py",
      "title": "baseConverter",
      "section": "A&D",
      "relative_path": "baseConverter.py",
      "summary": "In this A&D project, I work with data structure. I implement functions such as baseConverter. I build reusable functions and work with stack operations.",
      "line_count": 19,
      "size_label": "0.4 KB",
      "modified": "2025-10-13T21:54:07.334670",
      "modified_label": "Oct 13, 2025",
      "file_url": "files/a-d/baseConverter.py",
      "preview": "from StackClass import Stack\n\ndef baseConverter(decNumber,base):\n    digits = \"0123456789ABCDEF\"\n\n    remstack = Stack()\n\n    while decNumber > 0:\n        rem = decNumber % base\n        remstack.push(rem)\n        decNumber = decNumber // base\n\n    newString = \"\"\n    while not remstack.isEmpty():\n        newString = newString + digits[remstack.pop()]\n\n    return newString\n\nprint(baseConverter(9,8))",
      "tags": [
        "A&D",
        "Python",
        "data structure"
      ]
    },
    {
      "id": "a-d-basicturtle-py",
      "title": "basicTurtle",
      "section": "A&D",
      "relative_path": "basicTurtle.py",
      "summary": "In this project, I focus on turtle Basics. I draw graphics with turtle.",
      "line_count": 21,
      "size_label": "0.3 KB",
      "modified": "2025-09-24T20:54:45.957203",
      "modified_label": "Sep 24, 2025",
      "file_url": "files/a-d/basicTurtle.py",
      "preview": "\"\"\"\nTurtle Basics\n\"\"\"\nimport turtle\n\nt = turtle.Turtle()\nwin=turtle.Screen()\nfor i in range(20):\n    \n    t.color(\"red\")\n    t.forward(20)\n    t.right(100)\n    t.forward(50)\n    t.left(80)\n    t.color(\"blue\")\n    t.backward(30)\n    t.left(90)\n    t.color('green')\n    t.forward(120)\nt.forward(100)",
      "tags": [
        "A&D",
        "Python"
      ]
    },
    {
      "id": "a-d-bubblesort-py",
      "title": "bubbleSort",
      "section": "A&D",
      "relative_path": "bubbleSort.py",
      "summary": "In this A&D project, I work with sorting and algorithms. I implement functions such as bubbleSort. I build reusable functions.",
      "line_count": 7,
      "size_label": "0.2 KB",
      "modified": "2025-10-08T20:50:33.745962",
      "modified_label": "Oct 08, 2025",
      "file_url": "files/a-d/bubbleSort.py",
      "preview": "def bubbleSort(alist):\n    for passnum in range(len(alist)-1,0,-1):\n        for i in range(passnum):\n            if alist[i]>alist[i+1]:\n                temp = alist[i]\n                alist[i] = alist[i+1]\n                alist[i+1] = temp",
      "tags": [
        "A&D",
        "Python",
        "sorting",
        "algorithms"
      ]
    },
    {
      "id": "a-d-cryptoexercise-py",
      "title": "CryptoExercise",
      "section": "A&D",
      "relative_path": "CryptoExercise.py",
      "summary": "In this file, I share part of my A&D work. I implement functions such as attack. I build reusable functions.",
      "line_count": 34,
      "size_label": "1.4 KB",
      "modified": "2025-08-25T17:07:16.681707",
      "modified_label": "Aug 25, 2025",
      "file_url": "files/a-d/CryptoExercise.py",
      "preview": "code = \"\"\"lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr\njx ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk\nlmird jk xjubt trmui jx ibndt\n\nwb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj\nower m vjyshrbr rashmkmbwjk jkr cjnhd prner bj lr fnmhwxwrd mkd wkiswurd bj invp mk rabrkb bpmb pr vjnhd\nurmvp bpr ibmbr jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii ijnkd mkd ipmsrhrii ipmsr w dj kjb drry\nytirhx bpr xwkmh mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb bpmb bpr xjhhjcwko wi bpr sujsru\nmsshwvmbwjk mkd wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr riir-kvr jx jqwkmcmk qmurnbr cwhh\nurymwk wkbmvb\"\"\"\n\n#code = 'xultpaajcxitltlxaarpjhtiwtgxktghidhipxciwtvgtpilpitghlxiwiwtxggadds'\nfreq = {}\nfor letter in code:\n    if letter not in {' ','\\n','-'}:\n        if letter not in freq:\n            freq[letter] = 1\n        else:\n            freq[letter]+=1\n",
      "tags": [
        "A&D",
        "Python"
      ]
    },
    {
      "id": "a-d-exam1b-kollie-py",
      "title": "Exam1B Kollie",
      "section": "A&D",
      "relative_path": "Exam1B_Kollie.py",
      "summary": "In this project, I focus on CS337 Exam 1B Programming Question I did not consult with anyone or any internet source on the solution to this exam question. I define classes like Queue and Stack. I implement functions such as __init__, dequeue, enqueue, and isEmpty. I build reusable functions and work with queue operations.",
      "line_count": 60,
      "size_label": "1.2 KB",
      "modified": "2025-09-24T10:41:28.244921",
      "modified_label": "Sep 24, 2025",
      "file_url": "files/a-d/Exam1B_Kollie.py",
      "preview": "\"\"\"\nCS337 Exam 1B Programming Question\nI did not consult with anyone or any internet source on the solution to this exam question.\nName: Jallah Kollie                         \n\"\"\"\n\nclass Stack:\n    def __init__(self):\n        self.items = []\n\n    def isEmpty(self):\n        return self.items == []\n\n    def push(self, item):\n        self.items.append(item)\n\n    def pop(self):\n        return self.items.pop()\n\n    def peek(self):",
      "tags": [
        "A&D",
        "Python"
      ]
    },
    {
      "id": "a-d-fraction-py",
      "title": "fraction",
      "section": "A&D",
      "relative_path": "fraction.py",
      "summary": "In this file, I share part of my A&D work. I build reusable functions. I can run this script directly to produce output or visual results.",
      "line_count": 74,
      "size_label": "1.7 KB",
      "modified": "2025-09-02T21:11:02.304086",
      "modified_label": "Sep 02, 2025",
      "file_url": "files/a-d/fraction.py",
      "preview": "def gcd(m,n):\n    while m%n != 0:\n        oldm = m\n        oldn = n\n\n        m = oldn\n        n = oldm%oldn\n    return n\n\nclass Fraction:\n     def __init__(self,top,bottom):\n        if isinstance(top,int) and isinstance(bottom,int):\n            common = gcd(top,bottom)\n            self.num = top//common\n            self.den = bottom//common\n        else:\n            raise ValueError('value Error! The value has to be a integer')\n         \n\n     def __str__(self):",
      "tags": [
        "A&D",
        "Python"
      ]
    },
    {
      "id": "a-d-hashing-py",
      "title": "hashing",
      "section": "A&D",
      "relative_path": "hashing.py",
      "summary": "In this project, I focus on hashing. I define classes like hashTable. I implement functions such as __init__, __str__, loadFactor, and putInTable. I build reusable functions.",
      "line_count": 50,
      "size_label": "1.3 KB",
      "modified": "2025-10-02T12:04:33.942237",
      "modified_label": "Oct 02, 2025",
      "file_url": "files/a-d/hashing.py",
      "preview": "\"\"\"Hashing\"\"\"\n\nclass hashTable():\n    def __init__(self,size,hashfunction):\n        self.table =[None]*size\n        self.size =size\n        self.hashfunction=hashfunction\n\n    def putInTable(self, item):\n        key=self.hashfunction(item,self.size)\n        self.table[key]=item\n    \n    def searchTable(self,item):\n        key = self.hashfunction(item,self.size)\n        if self.table[key]==item:\n            return True\n        else:\n            return False\n        \n    def loadFactor(self):",
      "tags": [
        "A&D",
        "Python",
        "hashing",
        "lookup"
      ]
    },
    {
      "id": "a-d-insertionsort-py",
      "title": "insertionSort",
      "section": "A&D",
      "relative_path": "insertionSort.py",
      "summary": "In this A&D project, I work with sorting and algorithms. I implement functions such as insertionSort. I build reusable functions.",
      "line_count": 11,
      "size_label": "0.3 KB",
      "modified": "2025-10-10T10:28:56.023316",
      "modified_label": "Oct 10, 2025",
      "file_url": "files/a-d/insertionSort.py",
      "preview": "def insertionSort(alist):\n   for index in range(1,len(alist)):\n\n     currentvalue = alist[index]\n     position = index\n\n     while position>0 and alist[position-1]>currentvalue:\n         alist[position]=alist[position-1]\n         position = position-1\n\n     alist[position]=currentvalue",
      "tags": [
        "A&D",
        "Python",
        "sorting",
        "algorithms"
      ]
    },
    {
      "id": "a-d-kollie-exersice-py",
      "title": "Kollie exersice",
      "section": "A&D",
      "relative_path": "Kollie_exersice.py",
      "summary": "In this project, I focus on program exercise #1,2,5,13. I implement functions such as fac, fib, pascal, and revlis. I build reusable functions.",
      "line_count": 62,
      "size_label": "1.6 KB",
      "modified": "2025-09-22T10:29:14.693105",
      "modified_label": "Sep 22, 2025",
      "file_url": "files/a-d/Kollie_exersice.py",
      "preview": "\"\"\"Jallah Kollie Program exercise\n#1,2,5,13\"\"\"\n\n#1) Write a recursive function to compute the factorial of a number \n\ndef fac(n):\n    if n !=0: #base case\n        return fac(n-1)*n #factorial multiplication\n    else:\n        return 1\n\n    \nprint(fac(5))\n\n#2) Write a recursive function to reverse a list\n\ndef revlis(lis):\n     if len(lis) <=1:#base case\n         return lis\n     else:",
      "tags": [
        "A&D",
        "Python"
      ]
    },
    {
      "id": "a-d-kollie-limheap-py",
      "title": "Kollie limheap",
      "section": "A&D",
      "relative_path": "Kollie_limheap.py",
      "summary": "In this project, I focus on by submitting my files, I affirm that the solution to this exam are my own work and that I did not consult with anyone human or artificial in writing the code. I define classes like LimHeap. I implement functions such as __init__, delMin, insert, and minChild. I build reusable functions.",
      "line_count": 100,
      "size_label": "2.9 KB",
      "modified": "2025-11-17T18:58:59.718191",
      "modified_label": "Nov 17, 2025",
      "file_url": "files/a-d/Kollie_limheap.py",
      "preview": "'''\nBy submitting my files, I affirm that the solution to this exam are my own work \nand that I did not consult with anyone human or artificial in writing the code.\n\nName: Jallah Kollie \n\n'''\n\nclass LimHeap:\n    \n    def __init__(self,n):\n        self.nItem = n\n        self.heapList = [0]\n        self.currentSize = 0\n        \n        \n    def insert(self,k):\n        #insert all n items \n       if self.currentSize < self.nItem:     \n                self.heapList.append(k)",
      "tags": [
        "A&D",
        "Python"
      ]
    },
    {
      "id": "a-d-kollie-sortingtime-py",
      "title": "Kollie SortingTime",
      "section": "A&D",
      "relative_path": "Kollie_SortingTime.py",
      "summary": "In this project, I focus on 10-12-25. I implement functions such as bubbleSort, insertionSort, and mergeSort. I include randomized behavior. I build reusable functions.",
      "line_count": 96,
      "size_label": "2.1 KB",
      "modified": "2025-10-12T16:44:08.153554",
      "modified_label": "Oct 12, 2025",
      "file_url": "files/a-d/Kollie_SortingTime.py",
      "preview": "'''Jallah Kollie 10-12-25'''\nimport random\nimport time\n\n\nOrglis= [random.randint(0,1000) for _ in range(500)]\n#make copies of the list\nlis1 = Orglis[:]\nlis2 = Orglis[:]\nlis3 = Orglis[:]\n\n#bubble execution\ndef bubbleSort(alist):\n    for passnum in range(len(alist)-1,0,-1):\n        for i in range(passnum):\n            if alist[i]>alist[i+1]:\n                temp = alist[i]\n                alist[i] = alist[i+1]\n                alist[i+1] = temp\n#execution time",
      "tags": [
        "A&D",
        "Python",
        "sorting",
        "algorithms"
      ]
    },
    {
      "id": "a-d-kolliebfs-py",
      "title": "KollieBFS",
      "section": "A&D",
      "relative_path": "KollieBFS.py",
      "summary": "In this A&D project, I work with graph and network. I implement functions such as allPairs and bfs. I build reusable functions and work with queue operations.",
      "line_count": 50,
      "size_label": "1.2 KB",
      "modified": "2025-12-09T23:57:02.497551",
      "modified_label": "Dec 09, 2025",
      "file_url": "files/a-d/KollieBFS.py",
      "preview": "from vertex_graph2 import Graph, Vertex\nfrom pythondsBasic import Queue\nimport copy\n\ndef bfs(g,start):\n  start.setDistance(0)\n  start.setPred(None)\n  vertQueue = Queue()\n  vertQueue.enqueue(start)\n  while (vertQueue.size() > 0):\n    currentVert = vertQueue.dequeue()\n    \n    for nbr in currentVert.getConnections():\n        \n        if (nbr.getColor() == 'white'):\n            nbr.setColor('gray')\n            nbr.setDistance(currentVert.getDistance() + 1)\n            nbr.setPred(currentVert)\n            vertQueue.enqueue(nbr)\n    currentVert.setColor('black')",
      "tags": [
        "A&D",
        "Python",
        "graph",
        "network"
      ]
    },
    {
      "id": "a-d-kollieradix-py",
      "title": "KollieRadix",
      "section": "A&D",
      "relative_path": "KollieRadix.py",
      "summary": "In this project, I focus on radix program. September 10 2025. I include randomized behavior. I work with queue operations. I can run this script directly to produce output or visual results.",
      "line_count": 40,
      "size_label": "1.1 KB",
      "modified": "2025-09-10T23:16:21.828244",
      "modified_label": "Sep 10, 2025",
      "file_url": "files/a-d/KollieRadix.py",
      "preview": "'''Jallah Kollie Radix program.\n   September 10 2025'''\n\n#ones place -> x%10  hundreds place -> (x//100)%10  tens -> (x//10)%10 \nfrom QueueClass import Queue\nimport random\n#first make a list of random numbers\nmain = [random.randint(0,999) for _ in range(10)]\nprint('Unsorted: ', main)\n\n#create the bins\nbins = [Queue() for _ in range(10)]\n\norder = False\nplaceVal = 1\nwhile not order:\n    #loop through a copy of the list taking each element out and put it in a bin\n    for num in main[:]:\n        numOut = num\n        #identify the place value # of each item that is taken out of the list",
      "tags": [
        "A&D",
        "Python",
        "data structure",
        "simulation"
      ]
    },
    {
      "id": "a-d-kolliereview-py",
      "title": "KollieReview",
      "section": "A&D",
      "relative_path": "KollieReview.py",
      "summary": "In this project, I focus on 09-01-2025. I can run this script directly to produce output or visual results.",
      "line_count": 89,
      "size_label": "2.1 KB",
      "modified": "2025-08-31T00:16:50.261910",
      "modified_label": "Aug 31, 2025",
      "file_url": "files/a-d/KollieReview.py",
      "preview": "'''Jallah Kollie 09-01-2025'''\n\nfrom collections import Counter\nmytext = \"learning computer science is not unlike learning any other type of difficult subject matter.\"\n\n#Write code to do each of the following.\n#1. Create a list of the words in mytext in alphabetical order.\n#2. Create a string which is the same as mytext except that all the a's are replaced by X's.\n#3. Create a dictionary whose keys are letters and whose values are the frequency of that letter in mytext.\n#4. Create a string that has the words in mytext in reverse order.\n#5. Create a list whose elements are pairs of the form (word, num) where word is a word in mytext and num\n#   is the number of letters in word.\n#6. Create a string which is the same as mytext except that all the words are written backwards.\n#7. Create a 14 X 14 array in which the (i,j)th entry is 1 if the ith and jth words in mytext have the same\n#   number of letters and 0 otherwise.\n\n\n#1\nwords = mytext.split(' ')\nalph_ord = sorted(words)",
      "tags": [
        "A&D",
        "Python"
      ]
    },
    {
      "id": "a-d-linkedlistclass-py",
      "title": "LinkedListClass",
      "section": "A&D",
      "relative_path": "LinkedListClass.py",
      "summary": "In this A&D project, I work with data structure. I define classes like LinkedList. I implement functions such as __init__, add, append, and isEmpty. I build reusable functions.",
      "line_count": 75,
      "size_label": "1.7 KB",
      "modified": "2025-09-11T16:41:09.635434",
      "modified_label": "Sep 11, 2025",
      "file_url": "files/a-d/LinkedListClass.py",
      "preview": "from NodeClass import Node\n\nclass LinkedList:\n    def __init__(self):\n        self.head = None #the head is the first item in the list\n    \n    def isEmpty(self):\n        return self.head == None\n    \n    def add(self,item): #add to front of list\n        temp = Node(item)      #turn item into a Node\n        temp.setNext(self.head)  #new node points to old head of list\n        self.head = temp #new head of list\n        \n    def length(self):\n        current = self.head\n        count = 0\n        while current != None:\n            count = count + 1\n            current = current.getNext() #visit every node ",
      "tags": [
        "A&D",
        "Python",
        "data structure"
      ]
    },
    {
      "id": "a-d-mergesort-py",
      "title": "mergeSort",
      "section": "A&D",
      "relative_path": "mergeSort.py",
      "summary": "In this A&D project, I work with sorting and algorithms. I implement functions such as mergeSort. I build reusable functions.",
      "line_count": 32,
      "size_label": "0.7 KB",
      "modified": "2025-10-10T11:16:19.331517",
      "modified_label": "Oct 10, 2025",
      "file_url": "files/a-d/mergeSort.py",
      "preview": "def mergeSort(alist):\n    #print(\"Splitting \",alist)\n    if len(alist)>1:\n        mid = len(alist)//2\n        lefthalf = alist[:mid]\n        righthalf = alist[mid:]\n\n        mergeSort(lefthalf)\n        mergeSort(righthalf)\n\n        i=0\n        j=0\n        k=0\n        while i<len(lefthalf) and j<len(righthalf):\n            if lefthalf[i]<righthalf[j]:\n                alist[k]=lefthalf[i]\n                i=i+1\n            else:\n                alist[k]=righthalf[j]\n                j=j+1",
      "tags": [
        "A&D",
        "Python",
        "sorting",
        "algorithms"
      ]
    },
    {
      "id": "a-d-nodeclass-py",
      "title": "NodeClass",
      "section": "A&D",
      "relative_path": "NodeClass.py",
      "summary": "In this file, I share part of my A&D work. I define classes like Node. I implement functions such as __init__, getData, getNext, and setData. I build reusable functions.",
      "line_count": 16,
      "size_label": "0.4 KB",
      "modified": "2025-09-24T10:41:28.244310",
      "modified_label": "Sep 24, 2025",
      "file_url": "files/a-d/NodeClass.py",
      "preview": "class Node:\n    def __init__(self,initdata):#items in the list; each has a value and next\n        self.data = initdata\n        self.next = None\n\n    def getData(self):\n        return self.data\n\n    def getNext(self):\n        return self.next\n\n    def setData(self,newdata):\n        self.data = newdata\n\n    def setNext(self,newnext):\n        self.next = newnext",
      "tags": [
        "A&D",
        "Python"
      ]
    },
    {
      "id": "a-d-printerqueuesim-py",
      "title": "PrinterQueueSim",
      "section": "A&D",
      "relative_path": "PrinterQueueSim.py",
      "summary": "In this A&D project, I work with data structure and simulation. I implement functions such as newPrintTask and simulation. I include randomized behavior. I build reusable functions and work with queue operations.",
      "line_count": 43,
      "size_label": "1.0 KB",
      "modified": "2025-09-09T11:42:21.158696",
      "modified_label": "Sep 09, 2025",
      "file_url": "files/a-d/PrinterQueueSim.py",
      "preview": "from QueueClass import Queue\n\nimport random\nfrom PrinterTask import Printer, Task\n\n\ndef simulation(numSeconds, pagesPerMinute):\n\n    labprinter = Printer(pagesPerMinute)\n    printQueue = Queue()\n    waitingtimes = []\n\n    for currentSecond in range(numSeconds):\n\n      if newPrintTask():\n         task = Task(currentSecond)\n         printQueue.enqueue(task)\n\n      if (not labprinter.busy()) and \\\n                (not printQueue.isEmpty()):",
      "tags": [
        "A&D",
        "Python",
        "data structure",
        "simulation"
      ]
    },
    {
      "id": "a-d-printertask-py",
      "title": "PrinterTask",
      "section": "A&D",
      "relative_path": "PrinterTask.py",
      "summary": "In this file, I share part of my A&D work. I define classes like Printer and Task. I implement functions such as __init__, busy, getPages, and getStamp. I include randomized behavior. I build reusable functions.",
      "line_count": 37,
      "size_label": "1.1 KB",
      "modified": "2025-09-09T11:42:17.179186",
      "modified_label": "Sep 09, 2025",
      "file_url": "files/a-d/PrinterTask.py",
      "preview": "class Printer:\n    def __init__(self, ppm):\n        self.pagerate = ppm #pages per minute\n        self.currentTask = None\n        self.timeRemaining = 0\n\n    def tick(self): #Printer's internal clock\n        if self.currentTask != None:\n            self.timeRemaining = self.timeRemaining - 1\n            if self.timeRemaining <= 0:\n                self.currentTask = None\n\n    def busy(self):  #Is the printer busy?\n        if self.currentTask != None:\n            return True\n        else:\n            return False\n\n    def startNext(self,newtask):  #Start a new task\n        self.currentTask = newtask",
      "tags": [
        "A&D",
        "Python"
      ]
    },
    {
      "id": "a-d-pythondsbasic-py",
      "title": "pythondsBasic",
      "section": "A&D",
      "relative_path": "pythondsBasic.py",
      "summary": "In this file, I share part of my A&D work. I define classes like Deque, Queue, and Stack. I implement functions such as __init__, addFront, addRear, and dequeue. I build reusable functions and work with queue operations.",
      "line_count": 61,
      "size_label": "1.1 KB",
      "modified": "2025-12-09T19:01:07.481620",
      "modified_label": "Dec 09, 2025",
      "file_url": "files/a-d/pythondsBasic.py",
      "preview": "class Stack:\n    def __init__(self):\n        self.items = []\n\n    def isEmpty(self):\n        return self.items == []\n\n    def push(self, item):\n        self.items.append(item)\n\n    def pop(self):\n        return self.items.pop()\n\n    def peek(self):\n        return self.items[len(self.items)-1]\n\n    def size(self):\n        return len(self.items)\n\n",
      "tags": [
        "A&D",
        "Python"
      ]
    },
    {
      "id": "a-d-queueclass-py",
      "title": "QueueClass",
      "section": "A&D",
      "relative_path": "QueueClass.py",
      "summary": "In this A&D project, I work with data structure and simulation. I define classes like Queue. I implement functions such as __init__, dequeue, enqueue, and isEmpty. I build reusable functions and work with queue operations.",
      "line_count": 15,
      "size_label": "0.3 KB",
      "modified": "2025-09-09T11:20:21.546686",
      "modified_label": "Sep 09, 2025",
      "file_url": "files/a-d/QueueClass.py",
      "preview": "class Queue:\n    def __init__(self):\n        self.items = []\n\n    def isEmpty(self):\n        return self.items == []\n\n    def enqueue(self, item):\n        self.items.insert(0,item)\n\n    def dequeue(self):\n        return self.items.pop()\n\n    def size(self):\n        return len(self.items)",
      "tags": [
        "A&D",
        "Python",
        "data structure",
        "simulation"
      ]
    },
    {
      "id": "a-d-recursivemakechange-py",
      "title": "recursiveMakeChange",
      "section": "A&D",
      "relative_path": "recursiveMakeChange.py",
      "summary": "In this file, I share part of my A&D work. I implement functions such as recMC. I build reusable functions.",
      "line_count": 15,
      "size_label": "0.4 KB",
      "modified": "2025-09-25T11:27:59.773118",
      "modified_label": "Sep 25, 2025",
      "file_url": "files/a-d/recursiveMakeChange.py",
      "preview": "def recMC(coinValueList,change):\n   minCoins = change\n   if change in coinValueList:        \n       return 1\n   else:\n      for i in [c for c in coinValueList if c <= change]:\n          \n          numCoins = 1 + recMC(coinValueList,change-i) \n           \n          if numCoins < minCoins:\n            minCoins = numCoins\n   return minCoins\n\nprint(recMC([1,5,10,25],34))",
      "tags": [
        "A&D",
        "Python"
      ]
    },
    {
      "id": "a-d-sequentialsearch-py",
      "title": "sequentialSearch",
      "section": "A&D",
      "relative_path": "sequentialSearch.py",
      "summary": "In this A&D project, I work with search and algorithms. I implement functions such as sequentialSearch. I build reusable functions.",
      "line_count": 9,
      "size_label": "0.2 KB",
      "modified": "2025-10-02T12:07:20.604432",
      "modified_label": "Oct 02, 2025",
      "file_url": "files/a-d/sequentialSearch.py",
      "preview": "def sequentialSearch(alist, item):\n    for pos,num in enumerate(alist):\n        if num == item:\n            return True,pos\n    return print(False)\n        \n\n\nprint(sequentialSearch([1,2,3,6,8], 9))",
      "tags": [
        "A&D",
        "Python",
        "search",
        "algorithms"
      ]
    },
    {
      "id": "a-d-stackclass-py",
      "title": "StackClass",
      "section": "A&D",
      "relative_path": "StackClass.py",
      "summary": "In this project, I focus on list implementation of a stack. Rightmost element is the top. I define classes like Stack. I implement functions such as __init__, isEmpty, peek, and pop. I build reusable functions and work with stack operations.",
      "line_count": 20,
      "size_label": "0.4 KB",
      "modified": "2025-09-04T11:15:29.235564",
      "modified_label": "Sep 04, 2025",
      "file_url": "files/a-d/StackClass.py",
      "preview": "#List implementation of a stack. Rightmost element is the top.\n\nclass Stack:\n    def __init__(self):\n        self.items = []\n\n    def isEmpty(self):\n        return self.items == []\n\n    def push(self, item):\n        self.items.append(item)\n\n    def pop(self):\n        return self.items.pop()\n\n    def peek(self):\n        return self.items[len(self.items)-1]\n\n    def size(self):\n        return len(self.items)",
      "tags": [
        "A&D",
        "Python",
        "data structure"
      ]
    },
    {
      "id": "a-d-turtlesierpinski-py",
      "title": "turtleSierpinski",
      "section": "A&D",
      "relative_path": "turtleSierpinski.py",
      "summary": "In this file, I share part of my A&D work. I implement functions such as drawTriangle, getMid, and sierpinski. I draw graphics with turtle. I build reusable functions.",
      "line_count": 41,
      "size_label": "1.3 KB",
      "modified": "2025-09-24T20:54:48.880256",
      "modified_label": "Sep 24, 2025",
      "file_url": "files/a-d/turtleSierpinski.py",
      "preview": "from turtle import *\n\ndef drawTriangle(points,color,myTurtle):\n    myTurtle.fillcolor(color)\n    myTurtle.up()\n    myTurtle.goto(points[0])\n    myTurtle.down()\n    myTurtle.begin_fill()\n    myTurtle.goto(points[1])\n    myTurtle.goto(points[2])\n    myTurtle.goto(points[0])\n    myTurtle.end_fill()\n\ndef getMid(p1,p2):\n    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)\n\ndef sierpinski(points,degree,myTurtle):\n    colormap = ['blue','red','green','white','yellow',\n                'violet','orange']\n    drawTriangle(points,colormap[degree],myTurtle)",
      "tags": [
        "A&D",
        "Python"
      ]
    },
    {
      "id": "a-d-turtlespiral-py",
      "title": "turtleSpiral",
      "section": "A&D",
      "relative_path": "turtleSpiral.py",
      "summary": "In this file, I share part of my A&D work. I implement functions such as drawSpiral. I draw graphics with turtle. I build reusable functions.",
      "line_count": 13,
      "size_label": "0.3 KB",
      "modified": "2025-09-24T22:22:52.432850",
      "modified_label": "Sep 24, 2025",
      "file_url": "files/a-d/turtleSpiral.py",
      "preview": "from turtle import *\n\nmyTurtle = Turtle()\nmyWin = myTurtle.getscreen()\n\ndef drawSpiral(myTurtle, lineLen):\n    if lineLen > 0:\n        myTurtle.forward(lineLen)\n        myTurtle.right(90)\n        drawSpiral(myTurtle,lineLen-5)\n\ndrawSpiral(myTurtle,200)\nmyWin.exitonclick()",
      "tags": [
        "A&D",
        "Python"
      ]
    },
    {
      "id": "a-d-turtletree-py",
      "title": "turtleTree",
      "section": "A&D",
      "relative_path": "turtleTree.py",
      "summary": "In this A&D project, I work with tree and recursion. I implement functions such as tree. I draw graphics with turtle. I build reusable functions.",
      "line_count": 22,
      "size_label": "0.3 KB",
      "modified": "2025-09-24T23:11:49.716705",
      "modified_label": "Sep 24, 2025",
      "file_url": "files/a-d/turtleTree.py",
      "preview": "from turtle import *\n\n\ndef tree(branchLen,t):\n    \n    if branchLen > 5:\n        \n        t.forward(branchLen)\n        t.right(20)\n        tree(branchLen-15,t)\n        t.left(40)\n        tree(branchLen-10,t)\n        t.right(20)\n        t.backward(branchLen)\n        \n        \n\nt=Turtle()\nmyWin=t.getscreen()\nt.left(90)",
      "tags": [
        "A&D",
        "Python",
        "tree",
        "recursion"
      ]
    },
    {
      "id": "a-d-vertex-graph2-py",
      "title": "vertex graph2",
      "section": "A&D",
      "relative_path": "vertex_graph2.py",
      "summary": "In this project, I focus on graph and Vertex Classes. I define classes like Graph and Vertex. I implement functions such as __contains__, __init__, __iter__, and __str__. I build reusable functions.",
      "line_count": 89,
      "size_label": "2.1 KB",
      "modified": "2025-12-09T19:45:30.492362",
      "modified_label": "Dec 09, 2025",
      "file_url": "files/a-d/vertex_graph2.py",
      "preview": "\"\"\"\nGraph and Vertex Classes\n\"\"\"\nimport sys\nclass Vertex:\n    def __init__(self,key):\n        self.id = key\n        self.connectedTo = {}\n        self.color = 'white'\n        self.distance = sys.maxsize\n        self.pred = None\n        \n    def setColor(self,color):\n        self.color = color\n        \n    def setDistance(self,d):\n        self.distance = d\n\n    def setPred(self,p):\n        self.pred = p",
      "tags": [
        "A&D",
        "Python",
        "graph",
        "network"
      ]
    },
    {
      "id": "machine-learning-agatebasin-py",
      "title": "AgateBasin",
      "section": "Machine Learning",
      "relative_path": "AgateBasin.py",
      "summary": "In this project, I focus on k-means on Agate Basin Projectile Points. I read from local data files. I read input from files like projectile_points_Agate_Basin.txt. I can run this script directly to produce output or visual results.",
      "line_count": 46,
      "size_label": "1.1 KB",
      "modified": "2025-04-19T16:56:20.493361",
      "modified_label": "Apr 19, 2025",
      "file_url": "files/machine-learning/AgateBasin.py",
      "preview": "# -*- coding: utf-8 -*-\n\"\"\"\nK-means on Agate Basin Projectile Points\n\"\"\"\nfrom ClusterCounts import *\n\n\n#attribute 8\nrockDict ={'Chert':1, 'Quartz':2, 'KRF':3}\n#attribute 7\nbaseDict ={'Round':1,'Straight':2,'Concave':3,'Crushed':4}\n#attribute 6\nmarginsDict= {'Curved':1, 'Straight':2}\n\nagateEx =[]\ninfile = open('projectile_points_Agate_Basin.txt','r')\nfor line in infile:\n    if line != 'EOF':\n        lineList = line[:-1].split(',')\n        name = lineList[0]",
      "tags": [
        "Machine Learning",
        "Python",
        "clustering",
        "unsupervised learning"
      ]
    },
    {
      "id": "machine-learning-ann3-py",
      "title": "ANN3",
      "section": "Machine Learning",
      "relative_path": "ANN3.py",
      "summary": "In this project, I focus on a class provided by my professor Dr. Rauff. I define classes like ANN and Perceptron. I implement functions such as __init__, classify, construct, and outputNet. I include randomized behavior. I build reusable functions and build a perceptron-based learner.",
      "line_count": 154,
      "size_label": "5.1 KB",
      "modified": "2025-03-25T15:59:36.941361",
      "modified_label": "Mar 25, 2025",
      "file_url": "files/machine-learning/ANN3.py",
      "preview": "#Extension of Perceptron Class to 3-Layer ANN class\n#J. Rauff, March 2025\n\nfrom math import exp,sqrt\n\nclass Perceptron:\n    \"\"\"This perceptron class has sigmoid activation\"\"\"\n    \n    def __init__(self,inputs,bias=0):\n        self.inputs=inputs\n        self.weights=[]\n        self.bias=bias\n        \n        from random import random\n        for i in range(inputs):\n            self.weights.append(random()-0.5)\n        if self.bias != 0:\n             self.weights.append(random()-0.5)  # add a bias input line\n      \n    ",
      "tags": [
        "Machine Learning",
        "Python",
        "neural network",
        "classification"
      ]
    },
    {
      "id": "machine-learning-asante-py",
      "title": "Asante",
      "section": "Machine Learning",
      "relative_path": "Asante.py",
      "summary": "In this file, I share part of my Machine Learning work. I implement functions such as Make_moves, Placing, Play, and blocked. I include randomized behavior. I build reusable functions.",
      "line_count": 309,
      "size_label": "9.3 KB",
      "modified": "2025-02-06T00:33:52.035031",
      "modified_label": "Feb 06, 2025",
      "file_url": "files/machine-learning/Asante.py",
      "preview": "from AsanteClass import *\nfrom random import randint, choice\n\"\"\" Jallah Kollie. This is a Asante game that allows a human to play\nagainst a human\"\"\"\n\n#chooses the color tile\ndef Play():\n    game = Asante()\n    ans = input('Do I go first? y or n ')\n    if ans == 'y':\n        print('I choose Red :)')\n        comp_col = 'r'\n        user_col = 'b'\n    \n    else:\n        if ans=='n':\n#         make sure to make this case sensitive\n            user_col = input('what color do you want r or b?')\n        \n            if user_col == 'r':",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-asanteclass-py",
      "title": "AsanteClass",
      "section": "Machine Learning",
      "relative_path": "AsanteClass.py",
      "summary": "In this project, I focus on asante Game Base Uses the Asante class to represent the game board. I define classes like Asante. I implement functions such as __init__, blocked, move, and movingPhase. I build reusable functions.",
      "line_count": 140,
      "size_label": "4.4 KB",
      "modified": "2025-02-03T16:16:14.099439",
      "modified_label": "Feb 03, 2025",
      "file_url": "files/machine-learning/AsanteClass.py",
      "preview": "#Asante Game Base\n#Uses the Asante class to represent the game board\n\nclass Asante():\n    \"\"\"An Asante object represents an Asante game.\n        The board is conceptualized as a list. \"\"\"\n    \n    #Adjacency dictionary:\n    \"\"\"The key is board position and its value is a list of adjacent board positions\"\"\"\n    \n    adj ={0:[1,3,4],1:[0,2,4],2:[1,4,5],3:[0,4,6],4:[0,1,2,3,5,6,7,8],\n              5:[2,4,8],6:[3,4,7],7:[4,6,8],8:[4,5,7]}\n    \n    #List of winning lines\n    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]\n    \n    def __init__(self):\n               \n        self.board = list('000000000')         #Board positions:   0   1   2\n                                               #                   3   4   5",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-bam25-py",
      "title": "BAM25",
      "section": "Machine Learning",
      "relative_path": "BAM25.py",
      "summary": "In this project, I focus on bidirectional Associative Memory (BAM). I define classes like BAM. I implement functions such as __init__, associatexy, associateyx, and calcWeights. I build reusable functions.",
      "line_count": 63,
      "size_label": "1.3 KB",
      "modified": "2025-04-02T11:13:20.381121",
      "modified_label": "Apr 02, 2025",
      "file_url": "files/machine-learning/BAM25.py",
      "preview": "#Bidirectional Associative Memory (BAM)\nfrom MatrixClass import *\nclass BAM:\n    \n    def __init__(self,n,m):\n        self.n = n\n        self.m = m\n        self.weights = Matrix(n,m)\n    \n    def calcWeights(self,patt):\n        \n        for p in patt:\n            self.weights += p[0]*p[1].transpose()\n    \n    def associatexy(self,x):\n        return (self.weights.transpose()*x).sign()\n    \n    def associateyx(self,y):\n        return (self.weights*y).sign()\n    ",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-barrel-py",
      "title": "barrel",
      "section": "Machine Learning",
      "relative_path": "barrel.py",
      "summary": "In this project, I focus on barrel Question. I implement functions such as z. I include randomized behavior. I build reusable functions.",
      "line_count": 48,
      "size_label": "0.7 KB",
      "modified": "2025-03-01T13:10:51.531948",
      "modified_label": "Mar 01, 2025",
      "file_url": "files/machine-learning/barrel.py",
      "preview": "#Barrel Question\nfrom random import *\n\n#make the barrel and it's contents.\n\nbarrel =[]\nfor i in range(10000):\n    barrel.append('r')\n    \nfor i in range(8000):\n    barrel.append('b')\n    \nfor i in range(6000):\n    barrel.append('y')\n    \n    \nshuffle(barrel) #mix up the barrel\n\n#procedure Z\n",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-binarytreeclass-py",
      "title": "binaryTreeClass",
      "section": "Machine Learning",
      "relative_path": "binaryTreeClass.py",
      "summary": "In this Machine Learning project, I work with tree and recursion. I build reusable functions and model graph relationships. I can run this script directly to produce output or visual results.",
      "line_count": 171,
      "size_label": "5.4 KB",
      "modified": "2025-03-01T13:10:59.923110",
      "modified_label": "Mar 01, 2025",
      "file_url": "files/machine-learning/binaryTreeClass.py",
      "preview": "from DigraphClass import *\n\nclass BTNode(Node):\n    \"\"\"A BTNode has a name and a numerical value. It is created with its value.\"\"\"\n    def __init__(self, value = None):\n        \n        if value == None:   #The None node is special\n            self._name = 'None'\n        else:    \n            self._name = str(value)\n        self._value = value\n        \n    def get_value(self):\n        return self._value\n    \nclass BT(Digraph):  #Binary Tree Class\n    \"\"\"Binary trees are rooted trees in which each node has at most 2 children\"\"\"\n    \n    none = BTNode()   #The none node is a class attribute\n    ",
      "tags": [
        "Machine Learning",
        "Python",
        "tree",
        "recursion"
      ]
    },
    {
      "id": "machine-learning-birminghamparking-stats-py",
      "title": "BirminghamParking Stats",
      "section": "Machine Learning",
      "relative_path": "BirminghamParking_Stats.py",
      "summary": "In this project, I focus on birmingham Car Park Stats E. Hazard February 30,2020. I implement functions such as maxminOcc. I read from local data files and build reusable functions. I read input from files like Birminghamtab.txt and parking.txt.",
      "line_count": 75,
      "size_label": "1.8 KB",
      "modified": "2025-02-07T10:10:43.047200",
      "modified_label": "Feb 07, 2025",
      "file_url": "files/machine-learning/BirminghamParking_Stats.py",
      "preview": "\"\"\"\nBirmingham Car Park Stats\nE. Hazard\nFebruary 30,2020\n\"\"\"\nfrom math import inf\ninfile = open('parking.txt', 'r')\n\n# A dictionary of records keyed by car park name\nparkDict = {}  \n\n# A dictionary of capacities keyed by car park name\nparkCap = {}\n\n# A list of car park names\ncarparks = []  \n \nfor line in infile:\n    \n    dataList = line[:-1].split('\\t')",
      "tags": [
        "Machine Learning",
        "Python",
        "data analysis"
      ]
    },
    {
      "id": "machine-learning-buffon-3-d-py",
      "title": "Buffon 3-D",
      "section": "Machine Learning",
      "relative_path": "Buffon 3-D.py",
      "summary": "In this project, I focus on buffon in 3-D. I implement functions such as minkowski and throw_needles. I include randomized behavior. I build reusable functions.",
      "line_count": 20,
      "size_label": "0.6 KB",
      "modified": "2025-03-03T11:49:45.312297",
      "modified_label": "Mar 03, 2025",
      "file_url": "files/machine-learning/Buffon 3-D.py",
      "preview": "#Buffon in 3-D\nfrom random import random\ndef minkowski(p1,p2,n):\n    #Assume p1 and p2 are n-tuples representing coordinates in Euclidan n-space\n    total = 0\n    for i in range(n):\n        total += (p1[i]-p2[i])**2\n    return total**(1/n)\n\ndef throw_needles(num_needles):\n    in_circle = 0\n    for Needles in range(1, num_needles + 1):\n        x = random()\n        y = random()\n        z = random()\n        if minkowski((x,y,z),(0,0,0),3) <= 1:\n            in_circle += 1\n    #Counting needles in one quadrant only, so multiply by 4\n            \n    return 6*(in_circle/num_needles)",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-cardata-py",
      "title": "carData",
      "section": "Machine Learning",
      "relative_path": "carData.py",
      "summary": "In this project, I focus on car data. I read from local data files. I read input from files like car2.txt.",
      "line_count": 18,
      "size_label": "0.2 KB",
      "modified": "2025-04-07T11:05:32.755452",
      "modified_label": "Apr 07, 2025",
      "file_url": "files/machine-learning/carData.py",
      "preview": "#car data\n\ncfd ={}\nidnum = 0\ninfile = open('car2.txt','r')\nfor line in infile:\n    LL = line[:-1].split(',')\n    cfd[idnum]=LL\n    idnum +=1\ninfile.close()\n\nnewcar = ['med','low','2','more','big','high']",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-cardatabayes-py",
      "title": "carDataBayes",
      "section": "Machine Learning",
      "relative_path": "carDataBayes.py",
      "summary": "In this project, I focus on car data Bayes. I implement functions such as Bayes, ProbaGivenv, attValueList, and probValue. I read from local data files and build reusable functions. I read input from files like car2.txt.",
      "line_count": 79,
      "size_label": "1.9 KB",
      "modified": "2025-04-09T11:23:40.684214",
      "modified_label": "Apr 09, 2025",
      "file_url": "files/machine-learning/carDataBayes.py",
      "preview": "#Car data Bayes\n\ndef probValue(value,fd): #Calculates the probability of a particular class value\n    total = 0\n    for k in fd:\n        if fd[k][-1] == value:\n            total += 1\n    return total/len(fd.keys())\n\ndef attValueList(fd):  #Creates a list of the values taken by each attribute\n    numberOfatts = len(fd[0])\n    attList=[]\n    for i in range(numberOfatts):\n        atts =[]\n        \n        for k in fd:\n             if fd[k][i] not in atts:\n                atts.append(fd[k][i])\n        attList.append(atts)\n    return attList",
      "tags": [
        "Machine Learning",
        "Python",
        "classification",
        "probability"
      ]
    },
    {
      "id": "machine-learning-clustercounts-py",
      "title": "ClusterCounts",
      "section": "Machine Learning",
      "relative_path": "ClusterCounts.py",
      "summary": "In this Machine Learning project, I work with clustering and unsupervised learning. I define classes like Cluster and Example. I implement functions such as __init__, __str__, clusterCounts, and computeCentroid. I use NumPy for numeric computation and include randomized behavior. I build reusable functions.",
      "line_count": 186,
      "size_label": "5.7 KB",
      "modified": "2025-04-14T11:14:14.353845",
      "modified_label": "Apr 14, 2025",
      "file_url": "files/machine-learning/ClusterCounts.py",
      "preview": "import random\nimport numpy as np\n\n\ndef minkowskiDist(v1, v2, p):\n    \"\"\"Assumes v1 and v2 are equal-length arrays of numbers\n       Returns Minkowski distance of order p between v1 and v2\"\"\"\n    dist = 0.0\n    for i in range(len(v1)):\n        dist += abs(v1[i] - v2[i])**p\n    return dist**(1/p)\n    \n\n\n\nclass Example(object):\n    \n    def __init__(self, name, features, label = None):\n        #Assumes features is an array of floats\n        self.name = name",
      "tags": [
        "Machine Learning",
        "Python",
        "clustering",
        "unsupervised learning"
      ]
    },
    {
      "id": "machine-learning-congress-py",
      "title": "Congress ",
      "section": "Machine Learning",
      "relative_path": "Congress .py",
      "summary": "In this file, I share part of my Machine Learning work. I define classes like MC. I implement functions such as __init__, __str__, and vote. I read from local data files and build reusable functions. I read input from files like voting.txt.",
      "line_count": 45,
      "size_label": "0.9 KB",
      "modified": "2025-01-25T21:03:29.514679",
      "modified_label": "Jan 25, 2025",
      "file_url": "files/machine-learning/Congress .py",
      "preview": "class MC():\n    def __init__(self, label, party):\n        self.party = party\n        self.label = label\n        self.record = []\n        \n    def vote(self,n):\n        return self.record[n-1]\n        \n    \n    def __str__(self):\n        return 'Menmber of congress # {0} is a {1}.'.format(self.label, self.party)\n    \n    \n#this is how you do it usng a dictionary\n    \n'''infile = open('voting.txt', 'r')\nCongDict = {}\nlabel = 0\nfor line in infile:",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-crossvalidation-py",
      "title": "crossValidation",
      "section": "Machine Learning",
      "relative_path": "crossValidation.py",
      "summary": "In this project, I focus on holdout Cross-Validation. I implement functions such as BayesEval and separateData. I include randomized behavior. I read from local data files and build reusable functions.",
      "line_count": 53,
      "size_label": "1.4 KB",
      "modified": "2025-04-16T16:04:14.309223",
      "modified_label": "Apr 16, 2025",
      "file_url": "files/machine-learning/crossValidation.py",
      "preview": "#Holdout Cross-Validation \n\n#Making training and test files\nfrom random import randint\nfrom naiveBayes import *\n\ndef separateData(testSize,file_prefix):\n    original = file_prefix + '.txt'\n    train = file_prefix + 'Train.txt'\n    test = file_prefix + 'Test.txt'\n    infile = open(original,'r')\n    outtrain = open(train,'w')\n    outtest = open(test,'w')\n    counter = 0\n    for line in infile:\n        flip = randint(1,2)\n        if flip == 1:\n            if counter < testSize:\n                print(line[:-1], file = outtest)\n                counter+=1",
      "tags": [
        "Machine Learning",
        "Python",
        "classification",
        "probability"
      ]
    },
    {
      "id": "machine-learning-curvefit-py",
      "title": "curvefit",
      "section": "Machine Learning",
      "relative_path": "curvefit.py",
      "summary": "In this Machine Learning project, I work with curve fitting. I create charts or visualizations and use NumPy for numeric computation. I fit a polynomial curve to data and render a chart or plotted output. I read input from files like curve5.txt. I can run this script directly to produce output or visual results.",
      "line_count": 32,
      "size_label": "0.6 KB",
      "modified": "2025-05-06T21:50:41.817440",
      "modified_label": "May 06, 2025",
      "file_url": "files/machine-learning/curvefit.py",
      "preview": "import numpy as np\n\n\nx=[]\ny=[]\ninfile = open('curve5.txt','r')\nfor line in infile:\n    data = line.split()\n    x.append(float(data[0]))\n    y.append(float(data[1]))\ninfile.close()\n\nimport math\n#logy = [math.log(a,2) for a in y]\n#y=logy.copy()\nc = np.polyfit(x, y,4)\np = np.poly1d(c)\n\nimport matplotlib.pyplot as plt\nplt.scatter(x, y, label='Data')",
      "tags": [
        "Machine Learning",
        "Python",
        "curve fitting"
      ]
    },
    {
      "id": "machine-learning-cvrnn-py",
      "title": "CVRNN",
      "section": "Machine Learning",
      "relative_path": "CVRNN.py",
      "summary": "In this project, I focus on nearest Neighbor with Qualitative Attributes. I include randomized behavior. I read from local data files. I read input from files like voting.txt.",
      "line_count": 81,
      "size_label": "1.6 KB",
      "modified": "2025-04-01T21:48:44.749037",
      "modified_label": "Apr 01, 2025",
      "file_url": "files/machine-learning/CVRNN.py",
      "preview": "#Nearest Neighbor with Qualitative Attributes\n\n#Congressional Voting Records Data\nfrom NearestNeighbor import *\nfrom scalingFeatures import *\n\n#Make the feature dictionary\ncvr ={}\ninfile = open('voting.txt','r')\nindex = 0\nfor line in infile:\n    lineList = line[:-1].split(',')\n    cvr[index]=lineList\n    index+=1\ninfile.close()\n\n#Quantify data\n\nfor k in cvr.keys():\n    quant = []",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-derivative-py",
      "title": "derivative",
      "section": "Machine Learning",
      "relative_path": "derivative.py",
      "summary": "In this project, I focus on derivative Approximation. I implement functions such as derivative and poly. I create charts or visualizations. I render a chart or plotted output and read from local data files. I read input from files like scidata1.txt.",
      "line_count": 55,
      "size_label": "1.2 KB",
      "modified": "2025-05-02T13:43:14.028301",
      "modified_label": "May 02, 2025",
      "file_url": "files/machine-learning/derivative.py",
      "preview": "#Derivative Approximation\n\ndef  poly(x):\n    return x**3 -4*x**2 -3*x +2\n\ndef derivative(a, fcn, h):\n    return (fcn(a+h) - fcn(a-h))/(2*h)\n\nimport matplotlib.pyplot as plt\n\nplt.figure(1)\nplt.rcParams['lines.linewidth']=2.0\nplt.title('Function and Derivative')\nplt.xlabel('x')\nplt.ylabel('y')\nv=0\nh = 0.01\nx = []\ny = []\ny_prime =[]",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-digraphclass-py",
      "title": "DigraphClass",
      "section": "Machine Learning",
      "relative_path": "DigraphClass.py",
      "summary": "In this Machine Learning project, I work with graph and network. I define classes like Digraph, Edge, and Graph. I implement functions such as DFS, __init__, __str__, and add_edge. I build reusable functions and model graph relationships.",
      "line_count": 112,
      "size_label": "3.6 KB",
      "modified": "2025-03-01T13:10:59.927677",
      "modified_label": "Mar 01, 2025",
      "file_url": "files/machine-learning/DigraphClass.py",
      "preview": "class Node(object):\n    def __init__(self, name):\n        \"\"\"Assumes name is a string\"\"\"\n        self._name = name\n    def get_name(self):\n        return self._name\n    def __str__(self):\n        return self._name\n\nclass Edge(object):\n    def __init__(self, src, dest):\n        \"\"\"Assumes src and dest are Nodes\"\"\"\n        self._src = src\n        self._dest = dest\n    def get_source(self):\n        return self._src\n    def get_destination(self):\n        return self._dest\n    def __str__(self):\n        return self._src.get_name() + '->' + self._dest.get_name()",
      "tags": [
        "Machine Learning",
        "Python",
        "graph",
        "network"
      ]
    },
    {
      "id": "machine-learning-distributions-py",
      "title": "distributions",
      "section": "Machine Learning",
      "relative_path": "distributions.py",
      "summary": "In this file, I share part of my Machine Learning work. I use NumPy for numeric computation and include randomized behavior.",
      "line_count": 23,
      "size_label": "0.5 KB",
      "modified": "2025-03-10T10:29:57.791128",
      "modified_label": "Mar 10, 2025",
      "file_url": "files/machine-learning/distributions.py",
      "preview": "from random import gauss,uniform,randint,seed\nimport numpy as np\nseed(43)\nnums =[]\nfor i in range(5000):\n    nums.append(gauss(10,2))\n    \nmean = sum(nums)/len(nums)\nstdev = np.std(nums)\n\ndist ={'sd1':0,'sd2':0,'sd3':0}\nfor x in nums:\n    if abs(mean - x) < stdev:\n        dist['sd1'] += 1/5000\n    if abs(mean - x) < stdev*2:\n        dist['sd2'] += 1/5000\n    if abs(mean - x) < stdev*3:\n        dist['sd3'] += 1/5000\n\nnums = [int(round(x,0)) for x in nums]",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-evaluatingclassifiers-py",
      "title": "evaluatingClassifiers",
      "section": "Machine Learning",
      "relative_path": "evaluatingClassifiers.py",
      "summary": "In this project, I focus on evaluating Classifiers. I implement functions such as accuracy, get_stats, neg_pred_val, and pos_pred_val. I build reusable functions.",
      "line_count": 45,
      "size_label": "1.5 KB",
      "modified": "2025-03-31T11:05:48.788598",
      "modified_label": "Mar 31, 2025",
      "file_url": "files/machine-learning/evaluatingClassifiers.py",
      "preview": "#Evaluating Classifiers\n\ndef accuracy(true_pos, false_pos, true_neg, false_neg):\n    numerator = true_pos + true_neg\n    denominator = true_pos + true_neg + false_pos + false_neg\n    return numerator/denominator\n\ndef sensitivity(true_pos, false_neg):\n    try:\n        return true_pos/(true_pos + false_neg)\n    except ZeroDivisionError:\n        return float('nan')\n    \ndef specificity(true_neg, false_pos):\n    try:\n        return true_neg/(true_neg + false_pos)\n    except ZeroDivisionError:\n        return float('nan')\n    \ndef pos_pred_val(true_pos, false_pos):",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-ex-py",
      "title": "ex",
      "section": "Machine Learning",
      "relative_path": "ex.py",
      "summary": "In this project, I focus on finalP3.py Date: 05/09/2025 Authors: Noah Horner and Kevin Nshuti Genetic Algorithm + Perceptron Class Training This program compares Genetic Algorithm (GA) and Perceptron Learning Rule for training a perceptron to classify 5x5 letter patterns. I implement functions such as crossover, fitness, generate_population, and mutate. I include randomized behavior. I build reusable functions and build a perceptron-based learner.",
      "line_count": 136,
      "size_label": "4.4 KB",
      "modified": "2025-05-11T22:08:37.605126",
      "modified_label": "May 11, 2025",
      "file_url": "files/machine-learning/ex.py",
      "preview": "# finalP3.py\n# Date: 05/09/2025\n# Authors: Noah Horner and Kevin Nshuti\n# Genetic Algorithm + Perceptron Class Training\n# This program compares Genetic Algorithm (GA) and Perceptron Learning Rule\n# for training a perceptron to classify 5x5 letter patterns.\n\n\nfrom random import uniform, randint, choice\nfrom perceptronFinal import *\n\n\"\"\" \n(b) Range of random values:\n    We used random.uniform(-1.0, 1.0) to initialize each of the 25 weights. This keeps the weights in a balanced range, giving enough diversity without going\n    to extreme values that might cause unstable outputs.\n    \n(c) Fitness function:\n    The fitness of a chromosome is calculated by how many training patterns the perceptron correctly classifies when using the chromosome as its weight vector.\n    Since the perceptron uses the identity activation function, its output is a real number. To simulate binary classification, we interpret any output > 0.5 as class 1, and \u2264 0.5 as class 0.\n    For each pattern, if this thresholded prediction matches the true label, the chromosome earns one fitness point.",
      "tags": [
        "Machine Learning",
        "Python",
        "neural network",
        "classification"
      ]
    },
    {
      "id": "machine-learning-ex1-py",
      "title": "EX1",
      "section": "Machine Learning",
      "relative_path": "EX1.py",
      "summary": "In this project, I focus on exam 1, Feb. 24 2025. I implement functions such as barGraph, clique, find_maximal_clique, and shortPath. I create charts or visualizations. I render a chart or plotted output and read from local data files. I read input from files like people.txt.",
      "line_count": 207,
      "size_label": "5.4 KB",
      "modified": "2025-02-23T23:42:08.279251",
      "modified_label": "Feb 23, 2025",
      "file_url": "files/machine-learning/EX1.py",
      "preview": "''' Jallah Kollie, Exam 1, Feb. 24 2025'''\nimport matplotlib.pyplot as plt\nfrom Guttag14c import *\nfrom Guttag14d import *\n#1\nsocial = Digraph()\n#reads the file \ninfile = open('people.txt', 'r')\n\n#loops through the line file \nfor line in infile:\n    ppl = line[:-1].split('->')\n    \n    #start bode\n    sname = ppl[0]\n    #end node\n    ename = ppl[1]\n    #check if the sname node exist\n    if not social.get_node_from_name(sname):\n        social.add_node(Node(sname))",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-exam2-py",
      "title": "exam2",
      "section": "Machine Learning",
      "relative_path": "exam2.py",
      "summary": "In this project, I focus on CS235 Exam #2. I read from local data files. I read input from files like Raisin_Data.txt and raisinTestdata.txt. I can run this script directly to produce output or visual results.",
      "line_count": 60,
      "size_label": "1.4 KB",
      "modified": "2025-04-04T11:50:37.684866",
      "modified_label": "Apr 04, 2025",
      "file_url": "files/machine-learning/exam2.py",
      "preview": "#CS235 Exam #2\n#Name: Jallah Kollie\n\nfrom evaluatingClassifiers import *\nfrom NearestNeighbor import *\nfrom scalingFeature import *\n\nrd ={} #Feature Dictionary\nidnum = 0\ninfile = open('Raisin_Data.txt','r')\nfor line in infile:\n    linelist = line[:-1].split()\n    rd[idnum] = [float(x) for x in linelist[:-1]]+[linelist[-1]]\n    idnum+=1\ninfile.close()\n\ntestRaisins = [] #List of test raisins\ninfile = open('raisinTestdata.txt','r')\nfor line in infile:\n    linelist = line[:-1].split()",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-example-py",
      "title": "Example",
      "section": "Machine Learning",
      "relative_path": "Example.py",
      "summary": "In this file, I share part of my Machine Learning work. I create charts or visualizations. I render a chart or plotted output and read from local data files. I read input from files like function.txt. I can run this script directly to produce output or visual results.",
      "line_count": 28,
      "size_label": "0.5 KB",
      "modified": "2025-01-31T11:45:58.276247",
      "modified_label": "Jan 31, 2025",
      "file_url": "files/machine-learning/Example.py",
      "preview": "import matplotlib as plt\ninfile = open('function.txt')\nx,y=[],[]\nfor record in infile:\n    \n    xstr,ystr = record.split(',')\n    xval = float(xstr)\n    yval=float(ystr)\n    x.append(xval) \n    y.append(yval)\ninfile.close()\n    \nplt.figure(1)\nplt.rcParams['lines.linewidth']=2.0\nplt.title('funtion')\nplt.xlabel('x')\nplt.ylabel('y')\n\n\n",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-expressionga-py",
      "title": "expressionGA",
      "section": "Machine Learning",
      "relative_path": "expressionGA.py",
      "summary": "In this project, I focus on genetic Algorithm to Construct a Function. I implement functions such as assignFitness, crossover, fcn, and fitX. I include randomized behavior. I build reusable functions.",
      "line_count": 60,
      "size_label": "1.4 KB",
      "modified": "2025-04-29T12:55:46.755458",
      "modified_label": "Apr 29, 2025",
      "file_url": "files/machine-learning/expressionGA.py",
      "preview": "#Genetic Algorithm to Construct a Function\nfrom random import choice,randint\n\ndef generatePop(numpop,len_chrom):\n    pop = []\n    for i in range(numpop):\n        c = ''\n        for i in range(len_chrom):\n            c += choice(['+','-','*'])\n        pop.append(c)\n    return pop\n        \ndef value(c,x,y,z,w):\n    return eval('('+str(x)+c[0]+ str(y) +')'+c[1]+'('+str(z) +c[2]+str(w) + ')')\n\ndef fcn(x,y,z,w):\n    return (x+y) - (z*w)\n\ndef fitX(c):\n    val1 = value(c,2,3,4,5)",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-extrema-py",
      "title": "extrema",
      "section": "Machine Learning",
      "relative_path": "extrema.py",
      "summary": "In this project, I focus on finding extrema. I implement functions such as Extrema, derivative, and g. I build reusable functions.",
      "line_count": 47,
      "size_label": "1.2 KB",
      "modified": "2025-05-02T14:06:29.228077",
      "modified_label": "May 02, 2025",
      "file_url": "files/machine-learning/extrema.py",
      "preview": "#Finding extrema\n\n\ndef derivative(a, fcn, h):\n    return (fcn(a+h) - fcn(a-h))/(2*h)\n\ndef Extrema(f,a,b):\n    locmin =[]\n    locmax =[]\n    x = a\n    while x <= b:\n        d1 = derivative(x,f,.001)\n        d2 = derivative(x+.001,f,.001)\n        if d1*d2 < 0:\n            if d1 > 0:\n                locmax.append(x+.0005)\n            else:\n                locmin.append(x+.0005)\n        x +=.001\n    x=a",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-faces-py",
      "title": "Faces",
      "section": "Machine Learning",
      "relative_path": "Faces.py",
      "summary": "In this Machine Learning project, I work with graph, network, and neural network. I build a perceptron-based learner.",
      "line_count": 68,
      "size_label": "1.3 KB",
      "modified": "2025-03-19T15:10:47.013468",
      "modified_label": "Mar 19, 2025",
      "file_url": "files/machine-learning/Faces.py",
      "preview": "import math\nfrom perceptronClass import *\nfrom graphics1 import *\nfrom grayscale import *\n\nwin1=GraphWin(\"Face1\",500,500)\nF1=Image(Point(200,200),'Face1a.gif')\nF1.draw(win1)\n\nwin2=GraphWin(\"Face2\",500,500)\nF2=Image(Point(200,200),'Face2.gif')\nF2.draw(win2)\n\nwin3=GraphWin(\"Face3\",500,500)\nF3=Image(Point(200,200),'Face3.gif')\nF3.draw(win3)\n\nwin4=GraphWin(\"Face4\",500,500)\nF4=Image(Point(200,200),'Face2p.gif')\nF4.draw(win4)",
      "tags": [
        "Machine Learning",
        "Python",
        "graph",
        "network",
        "neural network",
        "classification"
      ]
    },
    {
      "id": "machine-learning-finalp1-py",
      "title": "finalP1",
      "section": "Machine Learning",
      "relative_path": "finalP1.py",
      "summary": "In this project, I focus on a class provided by my professor Dr. Rauff. I define classes like Particle. I implement functions such as __init__, make_objective, move, and objective. I create charts or visualizations and use NumPy for numeric computation. I render a chart or plotted output and build reusable functions.",
      "line_count": 90,
      "size_label": "2.8 KB",
      "modified": "2025-05-13T09:31:31.288277",
      "modified_label": "May 13, 2025",
      "file_url": "files/machine-learning/finalP1.py",
      "preview": "'''Jallah Kollie\n   Juan DelaPuente\nfinal program 1, May 13, 2025\n\nOur termination condition is 100\n\nFor the size of my swarm, I used 8 at first in which after running it one time seem to work but\nrunning it again, I saw the results were far from what I wanted. So I used 5000 as Dr. Rauff suggested and my\nresults became more consistent. I used 100 iterations. \n\n\n'''\n\n\nimport numpy as np\nimport random\nimport matplotlib.pyplot as plt\ndef poly(coeffs, x):\n    return coeffs[0]*x**3 + coeffs[1]*x**2 + coeffs[2]*x + coeffs[3]\n",
      "tags": [
        "Machine Learning",
        "Python",
        "optimization",
        "heuristics"
      ]
    },
    {
      "id": "machine-learning-finalp2-py",
      "title": "finalP2",
      "section": "Machine Learning",
      "relative_path": "finalP2.py",
      "summary": "In this project, I focus on juan DelaPuente final program 2, May 13, 2025. I implement functions such as fuzComp, fuzInt, fuzU, and muA. I create charts or visualizations. I render a chart or plotted output and build reusable functions.",
      "line_count": 150,
      "size_label": "3.3 KB",
      "modified": "2025-05-13T09:31:23.126362",
      "modified_label": "May 13, 2025",
      "file_url": "files/machine-learning/finalP2.py",
      "preview": "'''Jallah Kollie\n   Juan DelaPuente\nfinal program 2, May 13, 2025'''\n\n'''fuzzy logic is a way of mimicing how humans solve problems by encoding\nexpireice based knowledge in the form of logical rules - (my notes)\n\nthe compliment of \u00b5B tell us about the elements that are not in the fuzzy set. So .75 is the degree of non\nmembership.\n\n'''\n\nimport matplotlib.pyplot as plt\n\n#creats muA function\ndef muA(x):\n    if x <=-4:\n        return 1\n    \n    elif x >= -4 and x <= 0:",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-finalp3-py",
      "title": "finalP3",
      "section": "Machine Learning",
      "relative_path": "finalP3.py",
      "summary": "In this project, I focus on juan DelaPuente final program 3, May 13, 2025 b) For our random range we used -1 to 1 becuase we didn't want the number to be too big or too little. And making it go from -1 to 1 instead of 0 to 1 allows for the chromosome to also include negative number c) Our fitness frunction was the number of training patterns correctly classified by chromosomes d) My termination condition really doesn't seem to have much of a effect on my result. But when we changed my mutation rate to something other than.2, we saw that some instances classified the pattern as 0. In which I was able to alter the generations value to get a better result. Right now we have it at 50. g) A major difference between the weights of the two methods is the fact that PLR has more negative values in its classification, which could point to there being more negitive weights in the PLR. I define classes like Perceptron. I implement functions such as __init__, classify, crossover, and evolve. I include randomized behavior. I build reusable functions and build a perceptron-based learner.",
      "line_count": 228,
      "size_label": "6.7 KB",
      "modified": "2025-05-13T09:31:54.119216",
      "modified_label": "May 13, 2025",
      "file_url": "files/machine-learning/finalP3.py",
      "preview": "#Perceptron Class for Final Exam Question\n'''\nJallah Kollie\nJuan DelaPuente\nfinal program 3, May 13, 2025\n\nb) For our random range we used -1 to 1 becuase we didn't want the number to be too big or too little. And\nmaking it go from -1 to 1 instead of 0 to 1 allows for the chromosome to also include negative number\n\n\nc) Our fitness frunction was the number of training patterns correctly classified by chromosomes\n\n\nd) My termination condition really doesn't seem to have much of a effect on my result. But when we changed my mutation\nrate to something other than .2, we saw that some instances classified the pattern as 0. In which I was able to alter\nthe generations value to get a better result. Right now we have it at 50.\n\ng) A major difference between the weights of the two methods is the fact that PLR has more negative values in its classification, which\ncould point to there being more negitive weights in the PLR.\n",
      "tags": [
        "Machine Learning",
        "Python",
        "neural network",
        "classification"
      ]
    },
    {
      "id": "machine-learning-finalx1-py",
      "title": "finalX1",
      "section": "Machine Learning",
      "relative_path": "finalX1.py",
      "summary": "In this project, I focus on CS235 Final Exam 1 Name:. I create charts or visualizations and use NumPy for numeric computation. I fit a linear regression model and render a chart or plotted output. I read input from files like finalData.txt and peppers.txt. I can run this script directly to produce output or visual results.",
      "line_count": 123,
      "size_label": "3.2 KB",
      "modified": "2025-05-14T13:47:27.700366",
      "modified_label": "May 14, 2025",
      "file_url": "files/machine-learning/finalX1.py",
      "preview": "#CS235 Final Exam 1\n#Name:\n\n\nimport numpy as np\nimport matplotlib.pyplot as plt\nfrom sklearn.linear_model import LinearRegression\n\n\n#No additional imports are allowed\n\n# Read the file\nwith open('finalData.txt', 'r') as file:\n    lines = file.readlines()\n    \n    #chat gpt give me a new way to open and read the file :)\n\n# Extract the hotness category which is the last instance of the data\nhotness = [int(line.strip().split()[-1]) for line in lines]\n",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-finalx2-py",
      "title": "finalX2",
      "section": "Machine Learning",
      "relative_path": "finalX2.py",
      "summary": "In this project, I focus on CS235 Final Exam 2. I define classes like LLnode and LinkedList. I implement functions such as __init__, __str__, addNode, and find. I build reusable functions.",
      "line_count": 109,
      "size_label": "3.5 KB",
      "modified": "2025-05-14T13:53:25.539213",
      "modified_label": "May 14, 2025",
      "file_url": "files/machine-learning/finalX2.py",
      "preview": "#CS235 Final Exam 2\n\n#Name:\n\n#No imports are allowed\n\nclass LLnode(object):\n    \"\"\"A node is initialized with its value. Its head and tail are initialized as None\"\"\"\n    def __init__(self,value):\n        self.head=None\n        self.tail=None\n        self.value=value\n    \n    def __str__(self):\n        return str(self.head)+' | '+str(self.value)+' | '+str(self.tail)+'\\n'\n        \n    \nclass LinkedList(object):\n    \"\"\"A Linked list is initialized with its initial node (a LLnode object)\n       whose head is set to 0\"\"\"",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-food-py",
      "title": "food",
      "section": "Machine Learning",
      "relative_path": "food.py",
      "summary": "In this project, I focus on foodWeb Graph. I implement functions such as animal and prey. I read from local data files and build reusable functions. I read input from files like foodweb.txt.",
      "line_count": 86,
      "size_label": "1.6 KB",
      "modified": "2025-02-16T22:29:12.836244",
      "modified_label": "Feb 16, 2025",
      "file_url": "files/machine-learning/food.py",
      "preview": "#FoodWeb Graph\n\nfrom Guttag14c import *\n\nfw = Digraph()\ninfile = open('foodweb.txt','r')\nfor line in infile:\n    LL = line[:-1].split('->')\n    sname = LL[0]\n    dname = LL[1]\n    if not fw.get_node_from_name(sname):\n        fw.add_node(Node(sname))\n    sNode = fw.get_node_from_name(sname)\n    if not fw.get_node_from_name(dname):\n        fw.add_node(Node(dname))\n    dNode = fw.get_node_from_name(dname)\n    if dNode not in fw._edges[sNode]:\n        fw._edges[sNode].append(dNode)   \n        \n",
      "tags": [
        "Machine Learning",
        "Python",
        "graph",
        "network",
        "graph analysis"
      ]
    },
    {
      "id": "machine-learning-foodwebgraph-py",
      "title": "foodwebgraph",
      "section": "Machine Learning",
      "relative_path": "foodwebgraph.py",
      "summary": "In this project, I focus on foodWeb Graph. I implement functions such as eaten and eats. I read from local data files and build reusable functions. I read input from files like foodweb.txt.",
      "line_count": 74,
      "size_label": "1.8 KB",
      "modified": "2025-02-17T11:05:02.296945",
      "modified_label": "Feb 17, 2025",
      "file_url": "files/machine-learning/foodwebgraph.py",
      "preview": "#FoodWeb Graph\n\nfrom Guttag14c import *\n\nfw = Digraph()\ninfile = open('foodweb.txt','r')\nfor line in infile:\n    LL = line[:-1].split('->')\n    sname = LL[0]\n    dname = LL[1]\n    if not fw.get_node_from_name(sname):\n        fw.add_node(Node(sname))\n    sNode = fw.get_node_from_name(sname)\n    if not fw.get_node_from_name(dname):\n        fw.add_node(Node(dname))\n    dNode = fw.get_node_from_name(dname)\n    if dNode not in fw._edges[sNode]:\n        fw._edges[sNode].append(dNode)\n\ninfile.close()",
      "tags": [
        "Machine Learning",
        "Python",
        "graph",
        "network",
        "graph analysis"
      ]
    },
    {
      "id": "machine-learning-ga-py",
      "title": "GA",
      "section": "Machine Learning",
      "relative_path": "GA.py",
      "summary": "In this project, I focus on genetic Algorithm. I implement functions such as assignFitness, crossover, fit1, and generatePop. I include randomized behavior. I build reusable functions.",
      "line_count": 62,
      "size_label": "1.4 KB",
      "modified": "2025-04-29T12:55:45.103333",
      "modified_label": "Apr 29, 2025",
      "file_url": "files/machine-learning/GA.py",
      "preview": "#Genetic Algorithm\nfrom random import choice,randint\n\ndef generatePop(numpop,len_chrom):\n    pop = []\n    for i in range(numpop):\n        c = ''\n        for i in range(len_chrom):\n            c += choice(['1','0'])\n        pop.append(c)\n    return pop\n        \ndef fit1(c,goal):\n    fit = 0\n    for i in range(len(c)):\n        if c[i]==goal[i]:\n            fit +=1\n    return fit   \n\ndef assignFitness(pop,f,goal):",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-ga-assignment-py",
      "title": "GA Assignment",
      "section": "Machine Learning",
      "relative_path": "GA Assignment.py",
      "summary": "In this project, I focus on perceptron Class for Final Exam Question. I define classes like Perceptron. I implement functions such as __init__, classify, crossover, and evolve_colors. I include randomized behavior. I build reusable functions and build a perceptron-based learner.",
      "line_count": 188,
      "size_label": "5.2 KB",
      "modified": "2025-05-10T17:09:57.911016",
      "modified_label": "May 10, 2025",
      "file_url": "files/machine-learning/GA Assignment.py",
      "preview": "#Perceptron Class for Final Exam Question\n\nfrom random import random,randint\n\nclass Perceptron:\n    \"\"\"A perceptron is defined by its number of inputs and\nits activation function\"\"\"\n    \n    def __init__(self,inputs,activationFunction):\n        self.inputs=inputs\n        self.weights=[]\n        self.actFunc = activationFunction\n        \n        #Weights are initialized with random numbers in [-0.5, 0.5]\n        \n        for i in range(inputs):\n            self.weights.append(random()-0.5)\n        \n        \n    ",
      "tags": [
        "Machine Learning",
        "Python",
        "neural network",
        "classification"
      ]
    },
    {
      "id": "machine-learning-gasmolecules-py",
      "title": "gasMolecules",
      "section": "Machine Learning",
      "relative_path": "gasMolecules.py",
      "summary": "In this project, I focus on mixing of gas molecules. I define classes like Molecule. I implement functions such as __init__, distance, getColor, and setColor. I include randomized behavior. I build reusable functions.",
      "line_count": 57,
      "size_label": "1.7 KB",
      "modified": "2025-03-10T10:29:50.128223",
      "modified_label": "Mar 10, 2025",
      "file_url": "files/machine-learning/gasMolecules.py",
      "preview": "#Mixing of gas molecules\n\nfrom graphics import *\nfrom random import uniform,randint\nfrom math import sqrt\ndef distance(p1,p2):\n    return sqrt((p1.getX() - p2.getX())**2 + (p1.getY() - p2.getY())**2)\n\nclass Molecule():\n    \n    def __init__(self,x,y):\n        \n        self.pict = Circle(Point(x,y),0.5)\n        self.pict.setFill('red')\n        self.color = 'red'\n    def setColor(self,col):\n        self.color =col\n        self.pict.setFill(col)\n    def getColor(self):\n        return self.color",
      "tags": [
        "Machine Learning",
        "Python",
        "graph",
        "network"
      ]
    },
    {
      "id": "machine-learning-graph-on-board-feb-12-py",
      "title": "graph on board feb 12",
      "section": "Machine Learning",
      "relative_path": "graph on board feb 12.py",
      "summary": "In this project, I focus on the graph on the board feb 12. I model graph relationships.",
      "line_count": 11,
      "size_label": "0.3 KB",
      "modified": "2025-02-12T11:25:16.016001",
      "modified_label": "Feb 12, 2025",
      "file_url": "files/machine-learning/graph on board feb 12.py",
      "preview": "#The graph on the board feb 12\nfrom Guttag14c import *\n\np = 'ABCDEFGH'\nG = Digraph()\nfor name in p:\n    G.add_node(Node(name))\n\nG.add_edge(Edge(G._nodes[0], G._nodes[1]))\nG.add_edge(Edge(G._nodes[5], G._nodes[7]))\nG.add_edge(Edge(G.get_node_from_name('D'),G.get_node_from_name('E')) )",
      "tags": [
        "Machine Learning",
        "Python",
        "graph",
        "network"
      ]
    },
    {
      "id": "machine-learning-graphics-py",
      "title": "graphics",
      "section": "Machine Learning",
      "relative_path": "graphics.py",
      "summary": "In this project, I focus on simple object oriented graphics library The library is designed to make it very easy for novice programmers to experiment with computer graphics in an object oriented fashion. It is written by John Zelle for use with the book \"Python Programming: An Introduction to Computer Science\" (Franklin, Beedle & Associates). LICENSE: This is open-source software released under the terms of the GPL (http://www.gnu.org/licenses/gpl.html). PLATFORMS: The package is a wrapper around Tkinter and should run on any platform where Tkinter is available. INSTALLATION: Put this file somewhere where Python can see it. OVERVIEW: There are two kinds of objects in the library. The GraphWin class implements a window where drawing can be done and various GraphicsObjects are provided that can be drawn into a GraphWin. As a simple example, here is a complete program to draw a circle of radius 10 centered in a 100x100 window: -------------------------------------------------------------------- from graphics import * def main(): win = GraphWin(\"My Circle\", 100, 100) c = Circle(Point(50,50), 10) c.draw(win) win.getMouse() # Pause to view result win.close() # Close window when done main() -------------------------------------------------------------------- GraphWin objects support coordinate transformation through the setCoords method and pointer-based input through getMouse. The library provides the following graphical objects: Point Line Circle Oval Rectangle Polygon Text Entry (for text-based input) Image Various attributes of graphical objects can be set such as outline-color, fill-color and line-width. Graphical objects also support moving and hiding for animation effects. The library also provides a very simple class for pixel-based image manipulation, Pixmap. A pixmap can be loaded from a file and displayed using an Image object. Both getPixel and setPixel methods are provided for manipulating the image. DOCUMENTATION: For complete documentation, see Chapter 4 of \"Python Programming: An Introduction to Computer Science\" by John Zelle, published by Franklin, Beedle & Associates. Also see http://mcsp.wartburg.edu/zelle/python for a quick reference. I define classes like Circle, Entry, and GraphWin. I implement functions such as __autoflush, __checkOpen, __init__, and _draw. I build reusable functions.",
      "line_count": 942,
      "size_label": "28.7 KB",
      "modified": "2025-03-05T11:16:13.507167",
      "modified_label": "Mar 05, 2025",
      "file_url": "files/machine-learning/graphics.py",
      "preview": "# graphics.py\n\"\"\"Simple object oriented graphics library  \n\nThe library is designed to make it very easy for novice programmers to\nexperiment with computer graphics in an object oriented fashion. It is\nwritten by John Zelle for use with the book \"Python Programming: An\nIntroduction to Computer Science\" (Franklin, Beedle & Associates).\n\nLICENSE: This is open-source software released under the terms of the\nGPL (http://www.gnu.org/licenses/gpl.html).\n\nPLATFORMS: The package is a wrapper around Tkinter and should run on\nany platform where Tkinter is available.\n\nINSTALLATION: Put this file somewhere where Python can see it.\n\nOVERVIEW: There are two kinds of objects in the library. The GraphWin\nclass implements a window where drawing can be done and various\nGraphicsObjects are provided that can be drawn into a GraphWin. As a\nsimple example, here is a complete program to draw a circle of radius",
      "tags": [
        "Machine Learning",
        "Python",
        "graph",
        "network",
        "image processing"
      ]
    },
    {
      "id": "machine-learning-graphics1-py",
      "title": "graphics1",
      "section": "Machine Learning",
      "relative_path": "graphics1.py",
      "summary": "In this project, I focus on simple object oriented graphics library The library is designed to make it very easy for novice programmers to experiment with computer graphics in an object oriented fashion. It is written by John Zelle for use with the book \"Python Programming: An Introduction to Computer Science\" (Franklin, Beedle & Associates). LICENSE: This is open-source software released under the terms of the GPL (http://www.gnu.org/licenses/gpl.html). PLATFORMS: The package is a wrapper around Tkinter and should run on any platform where Tkinter is available. INSTALLATION: Put this file somewhere where Python can see it. OVERVIEW: There are two kinds of objects in the library. The GraphWin class implements a window where drawing can be done and various GraphicsObjects are provided that can be drawn into a GraphWin. As a simple example, here is a complete program to draw a circle of radius 10 centered in a 100x100 window: -------------------------------------------------------------------- from graphics import * def main(): win = GraphWin(\"My Circle\", 100, 100) c = Circle(Point(50,50), 10) c.draw(win) win.getMouse() # Pause to view result win.close() # Close window when done main() -------------------------------------------------------------------- GraphWin objects support coordinate transformation through the setCoords method and pointer-based input through getMouse. The library provides the following graphical objects: Point Line Circle Oval Rectangle Polygon Text Entry (for text-based input) Image Various attributes of graphical objects can be set such as outline-color, fill-color and line-width. Graphical objects also support moving and hiding for animation effects. The library also provides a very simple class for pixel-based image manipulation, Pixmap. A pixmap can be loaded from a file and displayed using an Image object. Both getPixel and setPixel methods are provided for manipulating the image. DOCUMENTATION: For complete documentation, see Chapter 4 of \"Python Programming: An Introduction to Computer Science\" by John Zelle, published by Franklin, Beedle & Associates. Also see http://mcsp.wartburg.edu/zelle/python for a quick reference. I define classes like Circle, Entry, and GraphWin. I implement functions such as __autoflush, __checkOpen, __init__, and _draw. I build reusable functions.",
      "line_count": 942,
      "size_label": "28.7 KB",
      "modified": "2025-03-19T14:37:46.179156",
      "modified_label": "Mar 19, 2025",
      "file_url": "files/machine-learning/graphics1.py",
      "preview": "# graphics.py\n\"\"\"Simple object oriented graphics library  \n\nThe library is designed to make it very easy for novice programmers to\nexperiment with computer graphics in an object oriented fashion. It is\nwritten by John Zelle for use with the book \"Python Programming: An\nIntroduction to Computer Science\" (Franklin, Beedle & Associates).\n\nLICENSE: This is open-source software released under the terms of the\nGPL (http://www.gnu.org/licenses/gpl.html).\n\nPLATFORMS: The package is a wrapper around Tkinter and should run on\nany platform where Tkinter is available.\n\nINSTALLATION: Put this file somewhere where Python can see it.\n\nOVERVIEW: There are two kinds of objects in the library. The GraphWin\nclass implements a window where drawing can be done and various\nGraphicsObjects are provided that can be drawn into a GraphWin. As a\nsimple example, here is a complete program to draw a circle of radius",
      "tags": [
        "Machine Learning",
        "Python",
        "graph",
        "network",
        "image processing"
      ]
    },
    {
      "id": "machine-learning-grayscale-py",
      "title": "grayscale",
      "section": "Machine Learning",
      "relative_path": "grayscale.py",
      "summary": "In this project, I focus on change to Gray Scale. I implement functions such as changeToGray. I build reusable functions.",
      "line_count": 23,
      "size_label": "0.6 KB",
      "modified": "2025-03-19T15:10:34.883424",
      "modified_label": "Mar 19, 2025",
      "file_url": "files/machine-learning/grayscale.py",
      "preview": "# -*- coding: utf-8 -*-\n\"\"\"\nChange to Gray Scale\n\"\"\"\nfrom graphics1 import *\n\n\ndef changeToGray (pic):\n    \"\"\"Returns a grayscale equivalent of an Image object (pic)\"\"\" \n #get dimensions of picture\n    height = pic.getHeight()\n    width=pic.getWidth()\n#Change to grayscale\n    for i in range(0,width):\n        for j in range(0,height):\n            r,g,b = pic.getPixel(i,j)\n            bright=int(round(0.299*r+0.587*g+0.114*b))\n            grayish=color_rgb(bright,bright,bright)\n            pic.setPixel(i,j,grayish)\n    return pic",
      "tags": [
        "Machine Learning",
        "Python",
        "graph",
        "network"
      ]
    },
    {
      "id": "machine-learning-grpah-py",
      "title": "grpah",
      "section": "Machine Learning",
      "relative_path": "grpah.py",
      "summary": "In this file, I share part of my Machine Learning work. I read from local data files and model graph relationships. I read input from files like g1.txt. I can run this script directly to produce output or visual results.",
      "line_count": 30,
      "size_label": "0.5 KB",
      "modified": "2025-02-16T22:29:12.831866",
      "modified_label": "Feb 16, 2025",
      "file_url": "files/machine-learning/grpah.py",
      "preview": "from Guttag14c import *\n\ninfile = open('g1.txt','r')\ng1 = Digraph()\n\nfor line in infile:\n    parts = line[:-1].split(',')\n    \n    if not g1.get_node_from_name(parts[0]):\n        srt = Node(parts[0])\n        g1.add_node(srt)\n        \n    if not g1.get_node_from_name(parts[1]):\n        end = Node(parts[1])\n        g1.add_node(end)\n        \n    if g1.get_node_from_name(parts[1]) not in g1._edges[g1.get_node_from_name(parts[0])]:\n        g1.add_edge(Edge(,end))\n        \n        ",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-guttag10-py",
      "title": "Guttag10",
      "section": "Machine Learning",
      "relative_path": "Guttag10.py",
      "summary": "In this project, I focus on code from page 179. I define classes like Grad, Int_set, and MIT_person. I implement functions such as __add__, __eq__, __hash__, and __init__. I build reusable functions.",
      "line_count": 322,
      "size_label": "8.7 KB",
      "modified": "2025-02-02T17:33:48.039367",
      "modified_label": "Feb 02, 2025",
      "file_url": "files/machine-learning/Guttag10.py",
      "preview": "# -*- coding: utf-8 -*-\n\n# # Code from page 179\nclass Toy(object):\n    def __init__(self):\n        self._elems = []\n    def add(self, new_elems):\n        \"\"\"new_elems is a list\"\"\"\n        self._elems += new_elems\n        \n    def size(self):\n        return len(self._elems)\n\n#print(type(Toy))\n#print(type(Toy.__init__), type(Toy.add), type(Toy.size))\n\n# # Code from page 180\n#t1 = Toy()\n#print(type(t1))\n#print(type(t1.add))",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-guttag14a-py",
      "title": "Guttag14a",
      "section": "Machine Learning",
      "relative_path": "Guttag14a.py",
      "summary": "In this project, I focus on figure 14-2 from page 284. I define classes like Item. I implement functions such as __init__, __str__, build_items, and density. I build reusable functions.",
      "line_count": 67,
      "size_label": "2.2 KB",
      "modified": "2025-02-07T11:07:02.188148",
      "modified_label": "Feb 07, 2025",
      "file_url": "files/machine-learning/Guttag14a.py",
      "preview": "# # Figure 14-2 from page 284\nclass Item(object):\n    def __init__(self, n, v, w):\n        self._name = n\n        self._value = v\n        self._weight = w\n    def get_name(self):\n        return self._name\n    def get_value(self):\n        return self._value\n    def get_weight(self):\n        return self._weight\n    def __str__(self):\n        return f'<{self._name}, {self._value}, {self._weight}>'\n\ndef value(item):\n    return item.get_value()\n\ndef weight_inverse(item):\n    return 1.0/item.get_weight()",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-guttag14b-py",
      "title": "Guttag14b",
      "section": "Machine Learning",
      "relative_path": "Guttag14b.py",
      "summary": "In this project, I focus on code from Figure 11-6. I implement functions such as choose_best, gen_powerset, get_binary_rep, and test_best. I build reusable functions.",
      "line_count": 56,
      "size_label": "1.7 KB",
      "modified": "2025-02-10T11:05:19.292875",
      "modified_label": "Feb 10, 2025",
      "file_url": "files/machine-learning/Guttag14b.py",
      "preview": "# # Code from Figure 11-6\ndef get_binary_rep(n, num_digits):\n   \"\"\"Assumes n and numDigits are non-negative ints\n      Returns a str of length numDigits that is a binary\n      representation of n\"\"\"\n   result = ''\n   while n > 0:\n      result = str(n%2) + result\n      n = n//2\n   if len(result) > num_digits:\n      raise ValueError('not enough digits')\n   for i in range(num_digits - len(result)):\n      result = '0' + result\n   return result\n\ndef gen_powerset(L):\n   \"\"\"Assumes L is a list\n      Returns a list of lists that contains all possible\n      combinations of the elements of L. E.g., if\n      L is [1, 2] it will return a list with elements",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-guttag14c-py",
      "title": "Guttag14c",
      "section": "Machine Learning",
      "relative_path": "Guttag14c.py",
      "summary": "In this file, I share part of my Machine Learning work. I define classes like Digraph, Edge, and Graph. I implement functions such as __init__, __str__, add_edge, and add_node. I build reusable functions and model graph relationships.",
      "line_count": 78,
      "size_label": "2.4 KB",
      "modified": "2025-02-12T11:02:40.013747",
      "modified_label": "Feb 12, 2025",
      "file_url": "files/machine-learning/Guttag14c.py",
      "preview": "class Node(object):\n    def __init__(self, name):\n        \"\"\"Assumes name is a string\"\"\"\n        self._name = name\n    def get_name(self):\n        return self._name\n    def __str__(self):\n        return self._name\n\nclass Edge(object):\n    def __init__(self, src, dest):\n        \"\"\"Assumes src and dest are Nodes\"\"\"\n        self._src = src\n        self._dest = dest\n    def get_source(self):\n        return self._src\n    def get_destination(self):\n        return self._dest\n    def __str__(self):\n        return self._src.get_name() + '->' + self._dest.get_name()",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-guttag14d-py",
      "title": "Guttag14d",
      "section": "Machine Learning",
      "relative_path": "Guttag14d.py",
      "summary": "In this file, I share part of my Machine Learning work. I implement functions such as DFS, print_path, shortest_path, and test_SP. I read from local data files and build reusable functions. I read input from files like foodweb.txt.",
      "line_count": 73,
      "size_label": "2.4 KB",
      "modified": "2025-02-17T11:07:18.342983",
      "modified_label": "Feb 17, 2025",
      "file_url": "files/machine-learning/Guttag14d.py",
      "preview": "from Guttag14c import *\n# # Figure 14-9 \ndef print_path(path):\n    \"\"\"Assumes path is a list of nodes\"\"\"\n    result = ''\n    for i in range(len(path)):\n        result = result + str(path[i])\n        if i != len(path) - 1:\n            result = result + '->'\n    return result \n\ndef DFS(graph, start, end, path, shortest, to_print = False):\n    \"\"\"Assumes graph is a Digraph; start and end are nodes;\n          path and shortest are lists of nodes\n       Returns a shortest path from start to end in graph\"\"\"\n    path = path + [start]\n    if to_print:\n        print('Current DFS path:', print_path(path))\n    if start == end:\n        return path",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-guttag14e-py",
      "title": "Guttag14e",
      "section": "Machine Learning",
      "relative_path": "Guttag14e.py",
      "summary": "In this file, I share part of my Machine Learning work. I implement functions such as BFS and test_SP. I build reusable functions and model graph relationships.",
      "line_count": 45,
      "size_label": "1.6 KB",
      "modified": "2025-02-24T11:08:37.938425",
      "modified_label": "Feb 24, 2025",
      "file_url": "files/machine-learning/Guttag14e.py",
      "preview": "from Guttag14c import *\n# # Figure 14-11 on page 303\ndef BFS(graph, start, end, to_print = False):\n    \"\"\"Assumes graph is a Digraph; start and end are nodes\n       Returns a shortest path from start to end in graph\"\"\"\n    init_path = [start]\n    path_queue = [init_path]\n    while len(path_queue) != 0:\n        #Get and remove oldest element in path_queue\n        tmp_path = path_queue.pop(0)\n        if to_print:\n            print('Current BFS path:', print_path(tmp_path))\n        last_node = tmp_path[-1]\n        if last_node == end:\n            return tmp_path\n        for next_node in graph.children_of(last_node):\n            if next_node not in tmp_path:\n                new_path = tmp_path + [next_node]\n                path_queue.append(new_path)\n    return None",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-guttag18-py",
      "title": "Guttag18",
      "section": "Machine Learning",
      "relative_path": "Guttag18.py",
      "summary": "In this file, I share part of my Machine Learning work. I implement functions such as check_pascal, est_pi, get_est, and roll_die. I use NumPy for numeric computation and include randomized behavior. I build reusable functions.",
      "line_count": 61,
      "size_label": "1.7 KB",
      "modified": "2025-03-10T10:29:44.194649",
      "modified_label": "Mar 10, 2025",
      "file_url": "files/machine-learning/Guttag18.py",
      "preview": "import random\nimport numpy as np\n\n# # Figure 18-1 on page 396\ndef roll_die():\n    return random.choice([1,2,3,4,5,6])\n\n# #Used later in chapter\n# def roll_die():\n#     return random.choice([1,1,2,3,3,4,4,5,5,5,6,6])\n\ndef check_pascal(num_trials):\n    \"\"\"Assumes num_trials is an int > 0\n       Prints an estimate of the probability of winning\"\"\"\n    num_wins = 0\n    for i in range(num_trials):\n        for j in range(24):\n            d1 = roll_die()\n            d2 = roll_die()\n            if d1 == 6 and d2 == 6:",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-guttag23a-py",
      "title": "Guttag23a",
      "section": "Machine Learning",
      "relative_path": "Guttag23a.py",
      "summary": "In this file, I share part of my Machine Learning work. I use pandas for tabular data handling. I can run this script directly to produce output or visual results.",
      "line_count": 111,
      "size_label": "2.6 KB",
      "modified": "2025-03-10T11:10:40.613340",
      "modified_label": "Mar 10, 2025",
      "file_url": "files/machine-learning/Guttag23a.py",
      "preview": "import pandas as pd\n\n# # Code on page 512\nwwc = pd.read_csv('wwc2019_q-f.csv')\nprint(wwc)\n#print(wwc.to_string())\n\n# # Code on page 513\n# for i in wwc.index:\n#     print(i)\n\n# # Code on page 514   \n#for c in wwc.columns:\n#     print(c)\n    \n# print(wwc.values)\n\n# # Code on page 515\n#creating a DataFrame\n# print(pd.DataFrame())",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-guttag23b-py",
      "title": "Guttag23b",
      "section": "Machine Learning",
      "relative_path": "Guttag23b.py",
      "summary": "In this file, I share part of my Machine Learning work. I implement functions such as get_country and get_games. I build reusable functions.",
      "line_count": 51,
      "size_label": "1.9 KB",
      "modified": "2025-03-10T11:35:56.907668",
      "modified_label": "Mar 10, 2025",
      "file_url": "files/machine-learning/Guttag23b.py",
      "preview": "from Guttag23a import *\n\n# # Code on page 525\n\n#print(wwc.loc[wwc['Winner'] == 'Sweden'])\n#Logical operators:  & = and, | = or, - = not\n#print(wwc.loc[(wwc['Winner'] == 'Sweden') | (wwc['Loser'] == 'Sweden')])\n\n\"\"\"Exercise: Write an expression that returns a DataFrame containing games\n             in which the USA but not France played.\"\"\"\n\nprint(wwc.loc[(wwc['Winner'] == 'USA') | -(wwc['Loser'] == 'France')])\n\n# # Code on page 526\ndef get_country(df, country):\n    \"\"\"df a DataFrame with series labeled Winner and Loser\n        country a str\n        returns a DataFrame with all rows in which country appears\n        in either the Winner or Loser column\"\"\"\n    return df.loc[(df['Winner'] == country) | (df['Loser'] == country)]",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-himmelblau-pso-py",
      "title": "himmelblau pso",
      "section": "Machine Learning",
      "relative_path": "himmelblau_pso.py",
      "summary": "In this project, I focus on particle swarming, 5/6/2025. I define classes like Particle. I implement functions such as __init__, himmelblau, move, and pso. I use NumPy for numeric computation and include randomized behavior. I build reusable functions.",
      "line_count": 53,
      "size_label": "1.6 KB",
      "modified": "2025-05-06T12:33:48.187341",
      "modified_label": "May 06, 2025",
      "file_url": "files/machine-learning/himmelblau_pso.py",
      "preview": "'''Jallah Kollie particle swarming, 5/6/2025'''\nimport numpy as np\nimport random\n\n#function\ndef himmelblau(x):\n    return (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2\n\nclass Particle:\n    def __init__(self, dim):\n        self.dim = dim\n        self.pos = np.random.uniform(0, 5, dim)\n        self.vel = np.zeros(dim)\n        self.best = self.pos.copy()\n\n    def update_best(self, obj_func):\n        if obj_func(self.pos) < obj_func(self.best):\n            self.best = self.pos.copy()\n\n    def move(self, global_best, alpha=1.5, beta=1.5):",
      "tags": [
        "Machine Learning",
        "Python",
        "optimization",
        "heuristics"
      ]
    },
    {
      "id": "machine-learning-house-price-py",
      "title": "House price",
      "section": "Machine Learning",
      "relative_path": "House price.py",
      "summary": "In this Machine Learning project, I work with prediction. I create charts or visualizations and use NumPy for numeric computation. I split data into training and test sets and fit a linear regression model. I can run this script directly to produce output or visual results.",
      "line_count": 100,
      "size_label": "2.3 KB",
      "modified": "2024-12-30T23:18:32.540110",
      "modified_label": "Dec 30, 2024",
      "file_url": "files/machine-learning/House price.py",
      "preview": "from pyexpat import features\n\nimport pandas as pd\nimport numpy as np\nimport seaborn as sns\nimport matplotlib.pyplot as plt\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.linear_model import LinearRegression\nfrom sklearn.metrics import mean_squared_error, r2_score\n\n#load data\ndata = pd.read_csv('realest.csv')\n#shows the first few lines of the data\nprint(data.head())\n#check basic info of the data\nprint(data.info())\n#checks for massive values/missing values\nprint(data.isnull().sum())\n\n#remove rows/columns with empty data",
      "tags": [
        "Machine Learning",
        "Python",
        "prediction"
      ]
    },
    {
      "id": "machine-learning-hw-py",
      "title": "HW",
      "section": "Machine Learning",
      "relative_path": "HW.py",
      "summary": "In this file, I share part of my Machine Learning work. I create charts or visualizations. I render a chart or plotted output and read from local data files. I read input from files like function.txt. I can run this script directly to produce output or visual results.",
      "line_count": 32,
      "size_label": "0.5 KB",
      "modified": "2025-02-03T10:43:36.407148",
      "modified_label": "Feb 03, 2025",
      "file_url": "files/machine-learning/HW.py",
      "preview": "import matplotlib.pyplot as plt\n\ninfile=open('function.txt','r')\nx,y=[],[]\nfor record in infile:\n    \n    xstr,ystr = record.split(',')\n    xval = float(xstr)\n    yval=float(ystr)\n    x.append(xval) \n    y.append(yval)\ninfile.close()\n    \nplt.figure(1)\nplt.rcParams['lines.linewidth']=2.0\nplt.title('Funtion Graph')\nplt.xlabel('x')\nplt.ylabel('y')\n\n",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-imageprocessing-py",
      "title": "ImageProcessing",
      "section": "Machine Learning",
      "relative_path": "ImageProcessing.py",
      "summary": "In this Machine Learning project, I work with neural network, classification, and image processing.",
      "line_count": 34,
      "size_label": "1.3 KB",
      "modified": "2025-03-27T12:29:07.722629",
      "modified_label": "Mar 27, 2025",
      "file_url": "files/machine-learning/ImageProcessing.py",
      "preview": "from perceptronClass import *\nfrom ANN3 import *\n\n#first set\nletters = [[0,1,1,1,1,1,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,1,1,1,1,1,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,[0,0]],\n           [0,1,1,1,1,0,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,1,1,1,1,1,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,1,1,1,1,1,0,[0,1]],\n           [0,1,1,1,1,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,1,1,0,[1,0]]]\n\n#creates my neural network \nneuralNet = ANN(49,26,2,.1)\n\nneuralNet.train(letters,.1, 8000) \n\ntestNet(neuralNet,letters)\n\n\n\n#camparing images \n\nBletters = [[0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,1,0,0,0,1,0,0,1,1,1,1,1,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,[0,0]],",
      "tags": [
        "Machine Learning",
        "Python",
        "neural network",
        "classification",
        "image processing"
      ]
    },
    {
      "id": "machine-learning-knapsack-py",
      "title": "knapsack",
      "section": "Machine Learning",
      "relative_path": "knapsack.py",
      "summary": "In this file, I share part of my Machine Learning work. I implement functions such as build_items, test_greedy, and test_greedys. I read from local data files and build reusable functions. I read input from files like loot.txt.",
      "line_count": 42,
      "size_label": "1.3 KB",
      "modified": "2025-02-08T00:49:48.549310",
      "modified_label": "Feb 08, 2025",
      "file_url": "files/machine-learning/knapsack.py",
      "preview": "from Guttag14a import *\ndef build_items():\n    names = ['clock', 'painting', 'radio', 'vase', 'book', 'computer', \n             'map', 'watch', 'TV', 'coffee_maker', 'diamond_ring', 'emu', 'duck']\n    values = [175, 90, 20, 50, 300, 200, \n              300, 125, 200, 110, 600, 65, 110]\n    weights = [10, 9, 4, 2, 1, 20, \n               5, 0.25, 20, 8, 0.10, 12, 3]\n    items = []\n    for i in range(len(values)):\n        items.append(Item(names[i], values[i], weights[i]))\n    return items\n\ninfile = open('loot.txt', 'r')\nname = []\nprice = []\nweight =[]\n\nfor line in infile:\n    name,price,weight =line.split('/t')",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-knapsackdynamic-py",
      "title": "knapsackDynamic",
      "section": "Machine Learning",
      "relative_path": "knapsackDynamic.py",
      "summary": "In this project, I focus on knapsack Problem using Dynamic Programming. I implement functions such as build_items. I use NumPy for numeric computation. I build reusable functions.",
      "line_count": 52,
      "size_label": "1.5 KB",
      "modified": "2025-02-10T11:43:27.323781",
      "modified_label": "Feb 10, 2025",
      "file_url": "files/machine-learning/knapsackDynamic.py",
      "preview": "#Knapsack Problem using Dynamic Programming\n\nfrom Guttag14a import *\nimport numpy as np\n\ndef build_items():\n    names = ['guitar', 'stereo','laptop']\n    values = [1500,3000,2000]\n    weights = [1,4,3]\n    Items = []\n    for i in range(len(values)):\n        Items.append(Item(names[i], values[i], weights[i]))\n    return Items\n\nItemList = build_items()\n\nstart = min(ItemList, key = lambda x: x.get_weight())\nItemList.remove(start)\nItemList = [start]+ItemList\n",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-knn-py",
      "title": "KNN",
      "section": "Machine Learning",
      "relative_path": "KNN.py",
      "summary": "In this project, I focus on KNN. I implement functions such as KNN, defineClasses, feature, and minkowskiDist. I read from local data files and build reusable functions.",
      "line_count": 95,
      "size_label": "2.4 KB",
      "modified": "2025-04-19T17:51:33.317303",
      "modified_label": "Apr 19, 2025",
      "file_url": "files/machine-learning/KNN.py",
      "preview": "# -*- coding: utf-8 -*-\n\"\"\"\nKNN \n\"\"\"\ndef feature(featureDatafile, splitCh =','):\n    infile=open(featureDatafile,'r')\n    \n    feature={}\n    ID=1\n    for line in infile:\n        feature[ID]=line[:-1].split(splitCh)\n        ID+=1\n    infile.close()\n    return feature\n\ndef minkowskiDist(v1, v2, p):\n    \"\"\"Assumes v1 and v2 are equal-length arrays of numbers\n       Returns Minkowski distance of order p between v1 and v2\"\"\"\n    dist = 0.0\n    for i in range(len(v1)):",
      "tags": [
        "Machine Learning",
        "Python",
        "classification",
        "nearest neighbors"
      ]
    },
    {
      "id": "machine-learning-kollie1-py",
      "title": "Kollie1",
      "section": "Machine Learning",
      "relative_path": "Kollie1.py",
      "summary": "In this project, I focus on CS235 Program 1,, 2/1/2025 worked with Doran and Marcellus. I define classes like Politician, Representative, and Senator. I implement functions such as __init__, __str__, collegial, and get_election_year. I build reusable functions.",
      "line_count": 86,
      "size_label": "2.8 KB",
      "modified": "2025-02-03T15:50:09.378843",
      "modified_label": "Feb 03, 2025",
      "file_url": "files/machine-learning/Kollie1.py",
      "preview": "'''CS235 Program 1, Jallah Kollie, 2/1/2025\nworked with Doran and Marcellus'''\n\n\n\n#this imports the parent class (person) for Politician\nfrom Guttag10 import Person    \n    \n# Finger exercise from page 194\nclass Politician(Person):\n    \"\"\" A politician is a person that can belong to a political party\"\"\"\n    \n    def __init__(self, name, party = None):\n        \"\"\"name and party are strings\"\"\"\n        self._name = name\n        self.party = party\n        \n     #identifies partyName as the party or Independent if no party and returns the politician's Name and their party    \n    def __str__(self):\n        partyName = self.party if self.party else 'Independent'",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-kollie2-py",
      "title": "Kollie2",
      "section": "Machine Learning",
      "relative_path": "Kollie2.py",
      "summary": "In this project, I focus on algerian Fire data. I implement functions such as barGraph, calculate_monthly_averages, plotNoon, and plotScatter. I create charts or visualizations. I render a chart or plotted output and read from local data files. I read input from files like Algerian_forest_fires_dataset.txt.",
      "line_count": 145,
      "size_label": "4.7 KB",
      "modified": "2025-02-10T02:10:18.155925",
      "modified_label": "Feb 10, 2025",
      "file_url": "files/machine-learning/Kollie2.py",
      "preview": "\"\"\"Jallah Kollie, Algerian Fire data\"\"\"\nimport matplotlib.pyplot as plt\nimport calendar\n\n# Open the Algerian forest fires data file\ninfile = open('Algerian_forest_fires_dataset.txt', 'r')\n\n\n# Initialize lists to store data for Bejaia with fire status,dates, and temps\nbejaia_data = []  # List for (date, temp, fire_status)\nDates = []\nbejaia_temps = []\nsidi_bel_abbes_temps = []\nbejaia_monthly_temps = {}\nsidi_bel_abbes_monthly_temps = {}\n\nfor line in infile:\n    #looks for the region name\n    if 'Bejaia Region Dataset' in line:\n        current_region = 'Bejaia'",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-llclass-py",
      "title": "LLclass",
      "section": "Machine Learning",
      "relative_path": "LLclass.py",
      "summary": "In this project, I focus on introduction to Linked Lists. I define classes like LLnode and LinkedList. I implement functions such as __init__, __str__, addNode, and findNode. I build reusable functions.",
      "line_count": 85,
      "size_label": "2.5 KB",
      "modified": "2025-05-07T11:02:03.209634",
      "modified_label": "May 07, 2025",
      "file_url": "files/machine-learning/LLclass.py",
      "preview": "#Introduction to Linked Lists\n\n\nclass LLnode(object):\n    \"\"\"A node is initialized with its value. Its head and tail are initialized as None\"\"\"\n    def __init__(self,value):\n        self.head=None\n        self.tail=None\n        self.value=value\n    \n    def __str__(self):\n        return str(self.head)+' | '+str(self.value)+' | '+str(self.tail)+'\\n'\n        \n    \nclass LinkedList(object):\n    \"\"\"A Linked list is initialized with its initial node (a LLnode object)\n       whose head is set to 0\"\"\"\n    def __init__(self,initialNode):\n        self.nodeCount=0\n        initialNode.head=0",
      "tags": [
        "Machine Learning",
        "Python",
        "data structure"
      ]
    },
    {
      "id": "machine-learning-llx-py",
      "title": "LLX",
      "section": "Machine Learning",
      "relative_path": "LLX.py",
      "summary": "In this project, I focus on linked List Exercise. I build reusable functions. I can run this script directly to produce output or visual results.",
      "line_count": 78,
      "size_label": "1.5 KB",
      "modified": "2025-05-08T12:02:26.749332",
      "modified_label": "May 08, 2025",
      "file_url": "files/machine-learning/LLX.py",
      "preview": "#Linked List Exercise\nfrom LLclass import *\n\ndata1 = [23,11,88,62,2,90,21,67]\ndata2 = ['banana', 'apricot', 'apple','peach','plum', 'kiwi','mango']\n\n#Using no other imports:\n\n#1.  Make a linked list called L1 from the data in data1.\n\nL1 = LinkedList(LLnode(data1[0]))\n\nfor i in data1:\n    L1.addNode(LLnode(i))\n    \n    \n\nprint(L1) \n    \n",
      "tags": [
        "Machine Learning",
        "Python",
        "data structure"
      ]
    },
    {
      "id": "machine-learning-llxsol-py",
      "title": "LLXsol",
      "section": "Machine Learning",
      "relative_path": "LLXsol.py",
      "summary": "In this project, I focus on linked List Exercise. I implement functions such as evalu, getNodeValues, join, and join2. I build reusable functions.",
      "line_count": 102,
      "size_label": "2.8 KB",
      "modified": "2025-05-14T13:52:14.780207",
      "modified_label": "May 14, 2025",
      "file_url": "files/machine-learning/LLXsol.py",
      "preview": "#Linked List Exercise\nfrom LLclass import *\n\ndata1 = [23,11,88,62,2,90,21,67]\ndata2 = ['banana', 'apricot', 'apple','peach','plum', 'kiwi','mango']\n\n#Using no other imports:\n\n#1.  Make a linked list called L1 from the data in data1.\nL1 = LinkedList(LLnode(data1[0]))\nfor v in data1[1:]:\n    L1.addNode(LLnode(v))\n\n#2.\t Make a linked list called L2 from the data in data2.\n\nL2 = LinkedList(LLnode(data2[0]))\nfor v in data2[1:]:\n    L2.addNode(LLnode(v))\n\n#3.  Make function join(LL1,LL2) that attaches a linked list LL2 to the end of linkd list LL1.",
      "tags": [
        "Machine Learning",
        "Python",
        "data structure"
      ]
    },
    {
      "id": "machine-learning-local-max-py",
      "title": "local max",
      "section": "Machine Learning",
      "relative_path": "local max.py",
      "summary": "In this file, I share part of my Machine Learning work. I implement functions such as Extrema and f. I build reusable functions.",
      "line_count": 45,
      "size_label": "0.6 KB",
      "modified": "2025-05-08T12:02:26.704223",
      "modified_label": "May 08, 2025",
      "file_url": "files/machine-learning/local max.py",
      "preview": "from derivative import *\nfrom math import cos,sin\n\ndef f(x):\n    return 2*cos(x-4)+3*(x-5)*sin((x-5)/2)\n\n\ndef Extrema(f,a,b):\n    s = a\n    g = b\n    h =0.01\n    local_min = []\n    local_max = []\n    \n    while s <= g:\n        ans1 = derivative(s,f,h)\n        ans2 = derivative(s+h,f,h)\n        \n        if ans1 * ans2 < 0:\n            if ans > 0:",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-lucciassignment-py",
      "title": "LucciAssignment",
      "section": "Machine Learning",
      "relative_path": "LucciAssignment.py",
      "summary": "In this Machine Learning project, I work with neural network and classification. I include randomized behavior. I build a perceptron-based learner. I can run this script directly to produce output or visual results.",
      "line_count": 38,
      "size_label": "0.8 KB",
      "modified": "2025-03-26T11:09:01.439531",
      "modified_label": "Mar 26, 2025",
      "file_url": "files/machine-learning/LucciAssignment.py",
      "preview": "from perceptronClass import *\nfrom random import random,shuffle\n\ntripple = []\n\n#add 20 random set of 3 numbers to a list\nfor i in range(20):\n    if i<=10:\n        x = random()\n        y = random()\n        z = random()\n        tripple.append([x,y,z,0])\n       \n       #split the numbers so it is linearly seperable \n    else:\n        x = random()\n        y = random()\n        z = random()-1\n        tripple.append([x,y,z,1])\n    ",
      "tags": [
        "Machine Learning",
        "Python",
        "neural network",
        "classification"
      ]
    },
    {
      "id": "machine-learning-matrixclass-py",
      "title": "MatrixClass",
      "section": "Machine Learning",
      "relative_path": "MatrixClass.py",
      "summary": "In this project, I focus on the Matrix Class. I define classes like Matrix. I implement functions such as POW, __add__, __init__, and __mul__. I build reusable functions.",
      "line_count": 87,
      "size_label": "2.3 KB",
      "modified": "2025-04-02T11:13:21.319327",
      "modified_label": "Apr 02, 2025",
      "file_url": "files/machine-learning/MatrixClass.py",
      "preview": "#The Matrix Class\n\nclass Matrix():\n    def __init__(self,rows,columns):\n        self.rows=rows\n        self.columns = columns\n        \n        mat=[]\n           \n        for i in range(rows):\n            row=[]\n            for j in range(columns):\n                row.append(0)\n            mat.append(row)\n        self.mat=mat\n    \n    def scalarMult(self,scalar):\n        sM=Matrix(self.rows,self.columns)\n        for i in range(self.rows):\n            for j in range(self.columns):",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-mean-median-mode-py",
      "title": "Mode",
      "section": "Machine Learning",
      "relative_path": "Mean/Median/Mode.py",
      "summary": "In this file, I share part of my Machine Learning work.",
      "line_count": 0,
      "size_label": "0.0 KB",
      "modified": "2024-10-28T23:33:43.793759",
      "modified_label": "Oct 28, 2024",
      "file_url": "files/machine-learning/Mean/Median/Mode.py",
      "preview": "# Empty file",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-multiregressionadvertising-py",
      "title": "multiregressionAdvertising",
      "section": "Machine Learning",
      "relative_path": "multiregressionAdvertising.py",
      "summary": "In this Machine Learning project, I work with regression and modeling. I create charts or visualizations and use NumPy for numeric computation. I fit a linear regression model and read from local data files. I read input from files like advertising.txt. I can run this script directly to produce output or visual results.",
      "line_count": 29,
      "size_label": "0.6 KB",
      "modified": "2025-05-01T11:18:59.833358",
      "modified_label": "May 01, 2025",
      "file_url": "files/machine-learning/multiregressionAdvertising.py",
      "preview": "import matplotlib.pylab as plt\nimport numpy as np\nfrom sklearn.linear_model import LinearRegression\nfrom sklearn import metrics\n\nest = LinearRegression(fit_intercept = True)\nadvfile = open('advertising.txt','r')\nheadings = advfile.readline().split()\nx=[]\ny=[]\nfor line in advfile:\n   lineList = line.split()\n   x.append([float(v) for v in lineList[:-1]])\n   y.append(float(lineList[-1]))\nadvfile.close()\nest.fit(x,y)\n\nprint(est.coef_,est.intercept_)\n\n",
      "tags": [
        "Machine Learning",
        "Python",
        "regression",
        "modeling"
      ]
    },
    {
      "id": "machine-learning-mushroom-py",
      "title": "mushroom",
      "section": "Machine Learning",
      "relative_path": "mushroom.py",
      "summary": "In this file, I share part of my Machine Learning work. I use pandas for tabular data handling. I read from local data files. I read input from files like mr.txt and unknown.txt.",
      "line_count": 40,
      "size_label": "0.5 KB",
      "modified": "2025-03-30T13:18:25.450436",
      "modified_label": "Mar 30, 2025",
      "file_url": "files/machine-learning/mushroom.py",
      "preview": "import pandas as pd\nfrom NearestNeighbor import *\nfrom scalingFeatures import *\n\n\n\nmr = open('mr.txt','r')\n\nmrd = {}\nidnum = 0\nfor line in mr:\n    ll = line[:-1].split(',')\n   \n    mrd[idnum] = ll[1:] + [ll[0]]\n    idnum +=1\n     \n    \nmr.close()\n\n",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-mushroomsnn-py",
      "title": "mushroomsNN",
      "section": "Machine Learning",
      "relative_path": "mushroomsNN.py",
      "summary": "In this project, I focus on mushrooms. I read from local data files. I read input from files like mr.txt and unknown.txt. I can run this script directly to produce output or visual results.",
      "line_count": 68,
      "size_label": "1.3 KB",
      "modified": "2025-04-04T06:58:55.420195",
      "modified_label": "Apr 04, 2025",
      "file_url": "files/machine-learning/mushroomsNN.py",
      "preview": "#Mushrooms\nfrom NearestNeighbor import *\nfrom scalingFeature import *\n#Feature dictionary\ninfile = open('mr.txt','r')\nmr ={}\nindex = 0\nfor line in infile:\n    linelist = line[:-1].split(',')\n    mr[index]=[ord(c) for c in linelist[1:]]+[linelist[0]]\n    index+=1\ninfile.close()\n\ninfile = open('unknown.txt','r')\nunk =[]\nfor line in infile:\n    linelist = line[:-1].split(',')\n    unk.append([ord(a) for a in linelist])\ninfile.close()\n",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-naivebayes-py",
      "title": "naiveBayes",
      "section": "Machine Learning",
      "relative_path": "naiveBayes.py",
      "summary": "In this project, I focus on bayes Classifier. I implement functions such as Bayes, ProbaGivenv, attValueList, and probValue. I build reusable functions.",
      "line_count": 61,
      "size_label": "1.6 KB",
      "modified": "2025-05-02T13:59:12.682017",
      "modified_label": "May 02, 2025",
      "file_url": "files/machine-learning/naiveBayes.py",
      "preview": "#Bayes Classifier\n\ndef probValue(value,fd): #Calculates the probability of a particular class value\n    total = 0\n    for k in fd:\n        if fd[k][-1] == value:\n            total += 1\n    return total/len(fd.keys())\n\ndef attValueList(fd):  #Creates a list of the values taken by each attribute\n    numberOfatts = len(fd[0])\n    attList=[]\n    for i in range(numberOfatts):\n        atts =[]\n        \n        for k in fd:\n             if fd[k][i] not in atts:\n                atts.append(fd[k][i])\n        attList.append(atts)\n    return attList",
      "tags": [
        "Machine Learning",
        "Python",
        "classification",
        "probability"
      ]
    },
    {
      "id": "machine-learning-nearestneighbor-py",
      "title": "NearestNeighbor",
      "section": "Machine Learning",
      "relative_path": "NearestNeighbor.py",
      "summary": "In this project, I focus on nearestNeighbor. I implement functions such as minkowskiDist and nearestNeighbor. I build reusable functions.",
      "line_count": 25,
      "size_label": "0.6 KB",
      "modified": "2025-03-31T11:43:01.012686",
      "modified_label": "Mar 31, 2025",
      "file_url": "files/machine-learning/NearestNeighbor.py",
      "preview": "#NearestNeighbor\nfrom math import inf\ndef minkowskiDist(v1, v2, p):\n    \"\"\"Assumes v1 and v2 are equal-length arrays of numbers\n       Returns Minkowski distance of order p between v1 and v2\"\"\"\n    dist = 0.0\n    for i in range(len(v1)):\n        dist += abs(v1[i] - v2[i])**p\n    return dist**(1/p)\n\ndef nearestNeighbor(new,feature):\n    nearest=inf\n    value = 0\n    for ID in feature:\n        old=[float(x) for x in feature[ID][:-1]]\n    \n        dist=minkowskiDist(new,old,len(old))\n    \n        if dist < nearest:\n            nearest=dist",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-newton-py",
      "title": "Newton",
      "section": "Machine Learning",
      "relative_path": "Newton.py",
      "summary": "In this file, I share part of my Machine Learning work. I implement functions such as Newton, derivative, f1, and f2. I build reusable functions.",
      "line_count": 30,
      "size_label": "0.6 KB",
      "modified": "2025-04-30T12:13:51.691327",
      "modified_label": "Apr 30, 2025",
      "file_url": "files/machine-learning/Newton.py",
      "preview": "def derivative(a,fcn,h):\n    return(fcn(a+h) - fcn(a-h))/(2*h)\n\n#Newton's Method\n\ndef Newton(fcn,guess,epsilon,h):\n    \"\"\"finds a root of fcn near guess using deravative approx\"\"\"\n    while abs(fcn(guess))> epsilon:\n        new = guess - fcn(guess)/derivative(guess,fcn,h)\n        guess = new\n    return guess\n\n\ndef f1(x):\n    return x**2 -4\n\nfrom math import sin,cos,log, e\n\ndef f2(x):\n    return cos(x + 2*log((abs(2*x)+0.02),10)) - 3*x/40*sin(x)*log(x**2+1,e)",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-nflclusters-py",
      "title": "NFLclusters",
      "section": "Machine Learning",
      "relative_path": "NFLclusters.py",
      "summary": "In this Machine Learning project, I work with clustering and unsupervised learning. I implement functions such as plotData. I create charts or visualizations. I render a chart or plotted output and read from local data files. I read input from files like NFLDraft.txt.",
      "line_count": 56,
      "size_label": "1.2 KB",
      "modified": "2025-04-14T11:14:16.781549",
      "modified_label": "Apr 14, 2025",
      "file_url": "files/machine-learning/NFLclusters.py",
      "preview": "from ClusterCounts import *\nimport matplotlib.pyplot as plt\n\ninfile=open('NFLDraft.txt','r')\n    \ndata={}\nID=1\nfor line in infile:\n    data[ID]=line[:-1].split(',')\n    ID+=1\ninfile.close()\n    \ndata1 ={}\nfor k in data:\n    data1[k]=[float(x) for x in data[k][:-1]]+[data[k][-1]]\n\nexNFL =makeExamples(data1)\n\nq=kmeans(exNFL,2)\nfor b in q:",
      "tags": [
        "Machine Learning",
        "Python",
        "clustering",
        "unsupervised learning"
      ]
    },
    {
      "id": "machine-learning-p3-py",
      "title": "P3",
      "section": "Machine Learning",
      "relative_path": "P3.py",
      "summary": "In this project, I focus on program 3 shraan game, March 4, 2025. I implement functions such as money, shRaan, shRaanTurn, and simShRaan. I use NumPy for numeric computation and include randomized behavior. I build reusable functions.",
      "line_count": 220,
      "size_label": "5.2 KB",
      "modified": "2025-03-10T07:34:25.192742",
      "modified_label": "Mar 10, 2025",
      "file_url": "files/machine-learning/P3.py",
      "preview": "'''Jallah Kollie, program 3 shraan game, March 4, 2025'''\nfrom random import *\nimport numpy as np\n\n\n#check2 = [6,5]\n#check3 = [5,4]\n\n\n\n\n#one turn of shraan\n\ndef shRaanTurn():\n    #simulates the three rolls\n    C1 = []\n    C2 = []\n    check1 = [6,5,4]\n    n = 5\n    turn = 0",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-p4-py",
      "title": "P4",
      "section": "Machine Learning",
      "relative_path": "P4.py",
      "summary": "In this project, I focus on program 4- Wine Quality, 3-28-2025. I use pandas for tabular data handling and include randomized behavior. I can run this script directly to produce output or visual results.",
      "line_count": 84,
      "size_label": "1.7 KB",
      "modified": "2025-03-28T07:14:31.201339",
      "modified_label": "Mar 28, 2025",
      "file_url": "files/machine-learning/P4.py",
      "preview": "'''Jallah Kollie program 4- Wine Quality, 3-28-2025'''\nimport pandas as pd\nfrom math import inf\nfrom NearestNeighbor import *\nfrom scalingFeatures import *\nfrom random import choice,seed\n\n#reads the file \nrw = pd.read_csv('winequality-red.csv', sep = ';')\n\n#removes 5 randomly selected instances from the file\nseed(15)\nlst = [a for a in range(1598)]\nrmlist = []\nfor i in range(5):\n    k = choice(lst)\n    lst.remove(k)\n    rmlist.append(k)\n\ntest = []",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-parking-py",
      "title": "parking",
      "section": "Machine Learning",
      "relative_path": "parking.py",
      "summary": "In this Machine Learning project, I work with data analysis. I read from local data files. I read input from files like parking.txt. I can run this script directly to produce output or visual results.",
      "line_count": 14,
      "size_label": "0.2 KB",
      "modified": "2025-02-08T00:49:48.526959",
      "modified_label": "Feb 08, 2025",
      "file_url": "files/machine-learning/parking.py",
      "preview": "infile = open('parking.txt','r')\ninfile.readline()\nlot =[]\nsev = []\nnum = []\ndate = []\ntime = []\nfor line in infile:\n    line.split(' ')\n    lot, sev,num, date = line.split('\\t')\n    print(lot)\n    \nfor i in num:\n    if i >",
      "tags": [
        "Machine Learning",
        "Python",
        "data analysis"
      ]
    },
    {
      "id": "machine-learning-particleclass-py",
      "title": "particleClass",
      "section": "Machine Learning",
      "relative_path": "particleClass.py",
      "summary": "In this file, I share part of my Machine Learning work. I define classes like Particle. I implement functions such as __init__, initialPos, and updateBest. I use NumPy for numeric computation and include randomized behavior. I build reusable functions.",
      "line_count": 30,
      "size_label": "0.9 KB",
      "modified": "2025-05-08T12:02:26.741394",
      "modified_label": "May 08, 2025",
      "file_url": "files/machine-learning/particleClass.py",
      "preview": "import numpy as np\nimport random\n\nclass Particle():\n    \"\"\"Particles are defined by the dimension of the space in which they fly\"\"\"\n    \n    def __init__(self, dim):\n        self.pos = np.array([0.0]*dim)\n        self.vel = np.array([0.0]*dim)\n        self.dim = dim\n        self.best = np.array([0.0]*dim)\n        \n    def initialPos(self, bound, firstQuad = True):\n        \"\"\"A particle's initial position is assigned randomly in (0,bound)\n        if the position should be in (-bound,bound) then set firstQuad = False\"\"\"\n        if firstQuad:\n            for i in range(self.dim):\n                self.pos[i]= bound*random()\n        else:\n            for i in range(self.dim):",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-particleswarm-py",
      "title": "ParticleSwarm",
      "section": "Machine Learning",
      "relative_path": "ParticleSwarm.py",
      "summary": "In this Machine Learning project, I work with optimization and heuristics. I implement functions such as himmelblau, makeSwarm, pso, and update_position. I include randomized behavior. I build reusable functions.",
      "line_count": 82,
      "size_label": "2.4 KB",
      "modified": "2025-05-06T08:57:39.702103",
      "modified_label": "May 06, 2025",
      "file_url": "files/machine-learning/ParticleSwarm.py",
      "preview": "from particleClass import *\n\ndef himmelblau(x):\n    return (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2\n\nfrom random import random  \n\ndef makeSwarm(size, dim, bound):\n    swarm = []\n    for _ in range(size):\n        p = Particle(dim)\n        p.initialPos(bound, firstQuad=True)  # positions between 0 and 5\n        p.best = np.copy(p.pos)  # initialize best to starting position\n        swarm.append(p)\n    return swarm\n\ndef update_velocity(p, g_best, alpha=2, beta=2):\n    new_velocity = np.zeros(p.dim)\n    for i in range(p.dim):\n        r1 = random()",
      "tags": [
        "Machine Learning",
        "Python",
        "optimization",
        "heuristics"
      ]
    },
    {
      "id": "machine-learning-perceptronclass-py",
      "title": "perceptronClass",
      "section": "Machine Learning",
      "relative_path": "perceptronClass.py",
      "summary": "In this project, I focus on a class provided by my professor Dr. Rauff. I define classes like Perceptron. I implement functions such as __init__, classify, identity, and outputValue. I include randomized behavior. I build reusable functions and build a perceptron-based learner.",
      "line_count": 160,
      "size_label": "4.9 KB",
      "modified": "2025-03-19T15:15:12.562760",
      "modified_label": "Mar 19, 2025",
      "file_url": "files/machine-learning/perceptronClass.py",
      "preview": "#Perceptron Class \n#A simple perceptron class with examples\n#J. Rauff -- March 2025\n\nclass Perceptron:\n    \"\"\"A perceptron is defined by its number of inputs and\nits activation function\"\"\"\n    \n    def __init__(self,inputs,activationFunction):\n        self.inputs=inputs\n        self.weights=[]\n        self.actFunc = activationFunction\n        \n        #Weights are initialized with random numbers in [-0.5, 0.5]\n        from random import random\n        for i in range(inputs):\n            self.weights.append(random()-0.5)\n        \n        \n    ",
      "tags": [
        "Machine Learning",
        "Python",
        "neural network",
        "classification"
      ]
    },
    {
      "id": "machine-learning-perceptronclassdelta-py",
      "title": "perceptronClassDelta",
      "section": "Machine Learning",
      "relative_path": "perceptronClassDelta.py",
      "summary": "In this project, I focus on a class provided by my professor Dr. Rauff. I define classes like Perceptron. I implement functions such as __init__, outputValue, printPat, and sigmoid. I include randomized behavior. I build reusable functions and build a perceptron-based learner.",
      "line_count": 107,
      "size_label": "3.0 KB",
      "modified": "2025-03-11T13:23:42.696329",
      "modified_label": "Mar 11, 2025",
      "file_url": "files/machine-learning/perceptronClassDelta.py",
      "preview": "#Perceptron Class with Delta Rule\n#A simple perceptron class with examples\n#J. Rauff -- March 2025\n\nclass Perceptron:\n    \"\"\"A perceptron is defined by its number of inputs and\nits activation function\"\"\"\n    \n    def __init__(self,inputs,activationFunction):\n        self.inputs=inputs\n        self.weights=[]\n        self.actFunc = activationFunction\n        \n        #Weights are initialized with random numbers in [-0.5, 0.5]\n        from random import random\n        for i in range(inputs):\n            self.weights.append(random()-0.5)\n        \n        \n    ",
      "tags": [
        "Machine Learning",
        "Python",
        "neural network",
        "classification"
      ]
    },
    {
      "id": "machine-learning-perceptronfinal-py",
      "title": "perceptronFinal",
      "section": "Machine Learning",
      "relative_path": "perceptronFinal.py",
      "summary": "In this project, I focus on perceptron Class for Final Exam Question. I define classes like Perceptron. I implement functions such as __init__, classify, crossover, and evolve. I include randomized behavior. I build reusable functions and build a perceptron-based learner.",
      "line_count": 226,
      "size_label": "6.6 KB",
      "modified": "2025-05-13T07:16:37.943926",
      "modified_label": "May 13, 2025",
      "file_url": "files/machine-learning/perceptronFinal.py",
      "preview": "#Perceptron Class for Final Exam Question\n\nfrom random import random,randint\n\nclass Perceptron:\n    \"\"\"A perceptron is defined by its number of inputs and\nits activation function\"\"\"\n    \n    def __init__(self,inputs,activationFunction):\n        self.inputs=inputs\n        self.weights=[]\n        self.actFunc = activationFunction\n        \n        #Weights are initialized with random numbers in [-0.5, 0.5]\n        \n        for i in range(inputs):\n            self.weights.append(random()-0.5)\n        \n        \n    ",
      "tags": [
        "Machine Learning",
        "Python",
        "neural network",
        "classification"
      ]
    },
    {
      "id": "machine-learning-pltfood-py",
      "title": "pltFood",
      "section": "Machine Learning",
      "relative_path": "pltFood.py",
      "summary": "In this project, I focus on creating a bar graph of food preferences from data in food.txt. I create charts or visualizations and use NumPy for numeric computation. I render a chart or plotted output and read from local data files. I read input from files like food.txt. I can run this script directly to produce output or visual results.",
      "line_count": 59,
      "size_label": "1.6 KB",
      "modified": "2025-02-03T11:09:22.430422",
      "modified_label": "Feb 03, 2025",
      "file_url": "files/machine-learning/pltFood.py",
      "preview": "\"\"\"Creating a bar graph of food preferences from data in food.txt\"\"\"\n\n\n#Import packages\nimport matplotlib.pyplot as plt\nimport numpy as np\nfrom random import random\n\n\n#Read data file and  create foods dictionary and foodList\ninfile = open('food.txt','r')\nfoods={}  #Initialize dictionary\nfoodList =[]  #Initialize foodList\nfor line in infile:\n    if line not in ['EOF']:\n        record= line.split()[:-1]\n        for food in record:\n            if food not in foods:\n                foods[food]=1  #Add food as key to dictionary with value 1\n                foodList.append(food)  #Add food to foodList",
      "tags": [
        "Machine Learning",
        "Python",
        "graph",
        "network",
        "graph analysis"
      ]
    },
    {
      "id": "machine-learning-pltintro-py",
      "title": "pltIntro",
      "section": "Machine Learning",
      "relative_path": "pltIntro.py",
      "summary": "In this file, I share part of my Machine Learning work. I create charts or visualizations. I render a chart or plotted output. I can run this script directly to produce output or visual results.",
      "line_count": 42,
      "size_label": "0.7 KB",
      "modified": "2025-01-31T11:20:34.527667",
      "modified_label": "Jan 31, 2025",
      "file_url": "files/machine-learning/pltIntro.py",
      "preview": "import matplotlib.pyplot as plt\nfrom math import sin\n\nplt.figure()\nplt.rcParams['lines.linewidth']=0.5\nplt.title('Graphy Thingy')\nplt.xlabel('X')\nplt.ylabel('Y')\n\nx=[]\ny=[]\nfor i in range(50):\n    x=x+[i]\n    j=i*2/7\n    y=y+[j]\n\nx2,y2=[],[]\nfor i in range(50):\n    x2=x2+[i]\n    j=-i*2/7",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-pltmystery-py",
      "title": "pltMystery",
      "section": "Machine Learning",
      "relative_path": "pltMystery.py",
      "summary": "In this file, I share part of my Machine Learning work. I create charts or visualizations. I render a chart or plotted output and read from local data files. I read input from files like mysteryFunction.txt. I can run this script directly to produce output or visual results.",
      "line_count": 31,
      "size_label": "0.5 KB",
      "modified": "2025-01-31T11:25:59.263906",
      "modified_label": "Jan 31, 2025",
      "file_url": "files/machine-learning/pltMystery.py",
      "preview": "import matplotlib.pyplot as plt\n\ninfile=open('mysteryFunction.txt','r')\nx,y=[],[]\nfor record in infile:\n    \n    xstr,ystr = record.split(',')\n    xval = float(xstr)\n    yval=float(ystr)\n    x.append(xval) \n    y.append(yval)\ninfile.close()\n    \nplt.figure(1)\nplt.rcParams['lines.linewidth']=2.0\nplt.title('Mystery Graph')\nplt.xlabel('x')\nplt.ylabel('y')\n\n",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-prac2-py",
      "title": "prac2",
      "section": "Machine Learning",
      "relative_path": "prac2.py",
      "summary": "In this project, I focus on algerian forest fires data. I implement functions such as plotNoon and plotScatter. I create charts or visualizations. I render a chart or plotted output and read from local data files. I read input from files like Algerian_forest_fires_dataset.txt.",
      "line_count": 141,
      "size_label": "3.4 KB",
      "modified": "2025-02-09T13:11:38.916505",
      "modified_label": "Feb 09, 2025",
      "file_url": "files/machine-learning/prac2.py",
      "preview": "\"\"\"Jallah Kollie, Algerian forest fires data\"\"\"\nimport matplotlib.pyplot as plt\n\n# Open the Algerian forest fires data file\ninfile = open('Algerian_forest_fires_dataset.txt', 'r')\n\n# Initialize lists to store data for each region\ndates = []\nbejaia_temps = []\nsidi_bel_abbes_temps = []\nred=[]\nblue=[]\n\n# Track the current region\ncurrent_region = None\n\n# Read the file line by line\nfor line in infile:\n   # line = line.strip()\n    ",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-practice-py",
      "title": "practice",
      "section": "Machine Learning",
      "relative_path": "practice.py",
      "summary": "In this file, I share part of my Machine Learning work. I render a chart or plotted output and read from local data files. I read input from files like Algerian_forest_fires_dataset.txt. I can run this script directly to produce output or visual results.",
      "line_count": 88,
      "size_label": "2.5 KB",
      "modified": "2025-02-09T23:35:49.403432",
      "modified_label": "Feb 09, 2025",
      "file_url": "files/machine-learning/practice.py",
      "preview": "import matplotlib.pyplot as plt\n\n# Open the Algerian forest fires data file\ninfile = open('Algerian_forest_fires_dataset.txt', 'r')\n\n\n# Initialize lists to store data for Bejaia with fire status\nbejaia_data = []  # List of tuples (date, temp, fire_status)\nDates = []\nbejaia_temps = []\nsidi_bel_abbes_temps = []\n\nfor line in infile:\n    if 'Bejaia Region Dataset' in line:\n        current_region = 'Bejaia'\n        continue\n    elif 'Sidi-Bel Abbes Region Dataset' in line:\n        current_region = 'Sidi-Bel Abbes'\n        continue\n    ",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-program-7-py",
      "title": "Program 7",
      "section": "Machine Learning",
      "relative_path": "Program 7.py",
      "summary": "In this project, I focus on program 7, May 2,2025. I use NumPy for numeric computation and use scikit-learn models and evaluation tools. I fit a linear regression model and read from local data files. I read input from files like lymphTest.txt and lymphTrain.txt. I can run this script directly to produce output or visual results.",
      "line_count": 128,
      "size_label": "2.4 KB",
      "modified": "2025-05-14T13:52:14.788208",
      "modified_label": "May 14, 2025",
      "file_url": "files/machine-learning/Program 7.py",
      "preview": "'''Jallah Kollie, Program 7, May 2,2025'''\n\nfrom naiveBayes import *\nfrom KNN import *\nfrom NearestNeighbor import *\nimport numpy as np\nfrom sklearn.linear_model import LinearRegression\nfrom sklearn import metrics\n\n\n#1\n\n#create feature dictionary\nfd ={} #Feature Dictionary\nidnum = 0\ninfile = open('lymphTrain.txt','r')\nfor line in infile:\n    linelist = line[:-1].split(',')\n    fd[idnum] = [int(x) for x in linelist]\n    idnum+=1",
      "tags": [
        "Machine Learning",
        "Python",
        "classification",
        "nearest neighbors",
        "probability"
      ]
    },
    {
      "id": "machine-learning-program5-6-py",
      "title": "Program5-6",
      "section": "Machine Learning",
      "relative_path": "Program5-6.py",
      "summary": "In this project, I focus on program 5-6, 04-21-25. I read from local data files. I read input from files like carBTest.txt, carBTrain.txt, and unknownCar.txt. I can run this script directly to produce output or visual results.",
      "line_count": 154,
      "size_label": "3.9 KB",
      "modified": "2025-04-21T14:59:45.638995",
      "modified_label": "Apr 21, 2025",
      "file_url": "files/machine-learning/Program5-6.py",
      "preview": "'''jallah Kollie, Program 5-6, 04-21-25'''\n\nfrom KNN import *\nfrom crossValidation import *\nfrom ClusterCounts import *\n\nToTacc = 0\n\n#simulates my 10 trials\nfor i in range(10):   \n    separateData(120, 'carB')\n\n\n    #gives each string a number \n    sdict = {'vhigh':8,'small':1, 'med':6,'high':10, 'low':7, '2':2, '3':3, '4':4,'5more':5, 'more':11, 'big':12}\n    \n    #reads the file and converts each string to integer \n    infile = open('carBTrain.txt','r')\n    FeatD = {}\n    iDx = 0",
      "tags": [
        "Machine Learning",
        "Python",
        "classification",
        "nearest neighbors",
        "clustering",
        "unsupervised learning"
      ]
    },
    {
      "id": "machine-learning-source-repos-thonnypython-program5-6-copy-py",
      "title": "Program5-6 copy",
      "section": "Machine Learning",
      "relative_path": "source/repos/ThonnyPython/Program5-6 copy.py",
      "summary": "In this project, I focus on program 5-6, 04-21-25. I read from local data files. I read input from files like carBTest.txt, carBTrain.txt, and unknownCar.txt. I can run this script directly to produce output or visual results.",
      "line_count": 154,
      "size_label": "3.9 KB",
      "modified": "2025-04-21T14:59:45.638995",
      "modified_label": "Apr 21, 2025",
      "file_url": "files/machine-learning/source/repos/ThonnyPython/Program5-6 copy.py",
      "preview": "'''jallah Kollie, Program 5-6, 04-21-25'''\n\nfrom KNN import *\nfrom crossValidation import *\nfrom ClusterCounts import *\n\nToTacc = 0\n\n#simulates my 10 trials\nfor i in range(10):   \n    separateData(120, 'carB')\n\n\n    #gives each string a number \n    sdict = {'vhigh':8,'small':1, 'med':6,'high':10, 'low':7, '2':2, '3':3, '4':4,'5more':5, 'more':11, 'big':12}\n    \n    #reads the file and converts each string to integer \n    infile = open('carBTrain.txt','r')\n    FeatD = {}\n    iDx = 0",
      "tags": [
        "Machine Learning",
        "Python",
        "classification",
        "nearest neighbors",
        "clustering",
        "unsupervised learning"
      ]
    },
    {
      "id": "machine-learning-qualitative-py",
      "title": "qualitative",
      "section": "Machine Learning",
      "relative_path": "qualitative.py",
      "summary": "In this project, I focus on dealing with qualitative data. I implement functions such as quant. I use pandas for tabular data handling and include randomized behavior. I read from local data files and build reusable functions. I read input from files like voting.txt.",
      "line_count": 44,
      "size_label": "0.7 KB",
      "modified": "2025-03-26T15:47:56.000933",
      "modified_label": "Mar 26, 2025",
      "file_url": "files/machine-learning/qualitative.py",
      "preview": "#dealing with qualitative data\nimport pandas as pd\n\n\n#1\n\ncongr = {}\n\nidnum = 1\n\nfile = open('voting.txt','r')\n\nfor line in file:\n    linelist = line[:-1].split(',')\n    congr[idnum] = linelist\n    idnum+=1\n    \nfile.close()\n\n#2",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-randomreview-py",
      "title": "RandomReview",
      "section": "Machine Learning",
      "relative_path": "RandomReview.py",
      "summary": "In this project, I focus on review of random. I include randomized behavior. I can run this script directly to produce output or visual results.",
      "line_count": 20,
      "size_label": "0.4 KB",
      "modified": "2025-03-10T10:29:24.263784",
      "modified_label": "Mar 10, 2025",
      "file_url": "files/machine-learning/RandomReview.py",
      "preview": "#Review of random\n\nfrom random import *\n\n#seed(4) #initialize what the random is going to start with\nprint(randint(5,20))\nprint(random())#prints a random number between 0 and 1\nprint(random())\n\nlst = [1,2,3,4,5,6,7,8]\nshuffle(lst)#shuffles the list\nprint(lst)\n\nprint(choice(lst))#randomly select something from the list\n\nprint(sample(lst,3)) #gives a random sample of the list\n\nprint(uniform(12,46)) #generates real numbers\n\nprint(gauss(mu=12, sigma=2.3))",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-regressionadvertising-py",
      "title": "regressionAdvertising",
      "section": "Machine Learning",
      "relative_path": "regressionAdvertising.py",
      "summary": "In this Machine Learning project, I work with regression and modeling. I implement functions such as regrline. I create charts or visualizations and use NumPy for numeric computation. I fit a linear regression model and render a chart or plotted output. I read input from files like advertising TV.txt, advertising newspaper.txt, and advertising radio.txt.",
      "line_count": 112,
      "size_label": "2.5 KB",
      "modified": "2025-04-23T11:07:26.463056",
      "modified_label": "Apr 23, 2025",
      "file_url": "files/machine-learning/regressionAdvertising.py",
      "preview": "import matplotlib.pylab as plt\nimport numpy as np\nfrom sklearn.linear_model import LinearRegression\nfrom sklearn import metrics\n\nest = LinearRegression(fit_intercept = True)\nadvfile = open('advertising TV.txt','r')\nheadings = advfile.readline().split()\nx=[]\ny=[]\nfor line in advfile:\n    x.append([float(line.split()[0])])\n    y.append(float(line.split()[1]))\nadvfile.close()\nest.fit(x,y)\n\nprint(est.coef_,est.intercept_)\ny_hat = est.predict(x)\nprint('Coefficient of Determination:',metrics.r2_score(y,y_hat))\n",
      "tags": [
        "Machine Learning",
        "Python",
        "regression",
        "modeling"
      ]
    },
    {
      "id": "machine-learning-review-py",
      "title": "Review",
      "section": "Machine Learning",
      "relative_path": "Review.py",
      "summary": "In this file, I share part of my Machine Learning work. I read from local data files. I read input from files like voting.txt. I can run this script directly to produce output or visual results.",
      "line_count": 17,
      "size_label": "0.2 KB",
      "modified": "2025-01-27T10:55:39.261994",
      "modified_label": "Jan 27, 2025",
      "file_url": "files/machine-learning/Review.py",
      "preview": "f = open('voting.txt','r')\nlis = []\nfor i in f:\n    lis.append(i)\n\nnew = lis.pop(249)\n \nnewLis = []\nnewLis.append(new)\nyes = newLis.pop(0)\nyes1 = str(yes)\nyes1.split(',')\n\nprint(yes1)",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-scaling-py",
      "title": "scaling",
      "section": "Machine Learning",
      "relative_path": "scaling.py",
      "summary": "In this project, I focus on scaling data for Nearest Neighbor classification. I implement functions such as linear_scale and z_scale. I use NumPy for numeric computation. I build reusable functions.",
      "line_count": 14,
      "size_label": "0.4 KB",
      "modified": "2025-03-14T11:01:13.269451",
      "modified_label": "Mar 14, 2025",
      "file_url": "files/machine-learning/scaling.py",
      "preview": "#Scaling data for Nearest Neighbor classification\n\nimport numpy as np\n\ndef z_scale(vals):\n    \"\"\"Assumes vals is a sequence of floats\"\"\"  \n    result = np.array(vals) - np.array(vals).mean()\n    return (result/np.std(result)).round(4)\n\ndef linear_scale(vals):\n    \"\"\"Assumes vals is a sequence of floats\"\"\"\n    vals = np.array(vals)\n    vals -= vals.min()\n    return (vals/vals.max()).round(4)",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-scalingfeature-py",
      "title": "scalingFeature",
      "section": "Machine Learning",
      "relative_path": "scalingFeature.py",
      "summary": "In this project, I focus on scaling data for Nearest Neighbor classification. I implement functions such as linear_scale, linscale, linscaleNew, and z_scale. I use NumPy for numeric computation. I build reusable functions.",
      "line_count": 80,
      "size_label": "2.3 KB",
      "modified": "2025-03-31T11:06:12.598533",
      "modified_label": "Mar 31, 2025",
      "file_url": "files/machine-learning/scalingFeature.py",
      "preview": "#Scaling data for Nearest Neighbor classification\n\nimport numpy as np\n\ndef linear_scale(vals):\n    \"\"\"Assumes vals is a sequence of floats\"\"\"\n    vals = np.array(vals)\n    vmin = vals.min() #Needed for new data\n    vmax = vals.max() #Needed for new data\n    if vmin != vmax:\n        vals = (vals - vmin)/(vmax - vmin)\n    else:\n        vals = vals - vmin\n    return vals,vmin,vmax   #returns the scaled data and the factors needed to scale new data\n\ndef z_scale(vals):\n    \"\"\"Assumes vals is a sequence of floats\"\"\"\n    mean = np.array(vals).mean()\n    std = np.array(vals).std()\n    result = np.array(vals) - np.array(vals).mean()",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-scalingfeatures-py",
      "title": "scalingFeatures",
      "section": "Machine Learning",
      "relative_path": "scalingFeatures.py",
      "summary": "In this project, I focus on scaling data for Nearest Neighbor classification. I implement functions such as linear_scale, linscale, linscaleNew, and z_scale. I use NumPy for numeric computation. I build reusable functions.",
      "line_count": 68,
      "size_label": "2.0 KB",
      "modified": "2025-03-24T11:07:00.003611",
      "modified_label": "Mar 24, 2025",
      "file_url": "files/machine-learning/scalingFeatures.py",
      "preview": "#Scaling data for Nearest Neighbor classification\n\nimport numpy as np\n\ndef linear_scale(vals):\n    \"\"\"Assumes vals is a sequence of floats\"\"\"\n    vals = np.array(vals)\n    vmin = vals.min() #Needed for new data\n    vmax = vals.max() #Needed for new data\n    vals = (vals - vmin)/(vmax - vmin)\n    return vals,vmin,vmax   #returns the scaled data and the factors needed to scale new data\n\ndef z_scale(vals):\n    \"\"\"Assumes vals is a sequence of floats\"\"\"\n    mean = np.array(vals).mean()\n    std = np.array(vals).std()\n    result = np.array(vals) - np.array(vals).mean()\n    return result/np.std(result),mean,std\n\n#Linear scaling: Linearly scales all the data",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-sideibel-py",
      "title": "SideiBel",
      "section": "Machine Learning",
      "relative_path": "SideiBel.py",
      "summary": "In this file, I share part of my Machine Learning work. I use pandas for tabular data handling. I can run this script directly to produce output or visual results.",
      "line_count": 13,
      "size_label": "0.3 KB",
      "modified": "2025-03-10T13:36:59.791445",
      "modified_label": "Mar 10, 2025",
      "file_url": "files/machine-learning/SideiBel.py",
      "preview": "import pandas as pd\n\nsbdf = pd.read_csv('SidiBelregion.csv')\nprint(sbdf)\n\nsbdf = sbdf.rename(columns = {' RH':'RH', 'Classes  ':'Classes',' Ws':'Ws'})\nprint(sbdf.columns)\n\nfirecount = 0\nfor d in sbdf['Classes']:\n    if 'n' not in d:\n        firecount+=1\nprint(firecount/len(sbdf.index))",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-sidibelsimilarity-py",
      "title": "SidiBelSimilarity",
      "section": "Machine Learning",
      "relative_path": "SidiBelSimilarity.py",
      "summary": "In this project, I focus on sidiBel Similarity. I implement functions such as scaleNew. I use pandas for tabular data handling. I build reusable functions.",
      "line_count": 44,
      "size_label": "1.1 KB",
      "modified": "2025-03-23T18:14:12.708305",
      "modified_label": "Mar 23, 2025",
      "file_url": "files/machine-learning/SidiBelSimilarity.py",
      "preview": "#SidiBel Similarity\nimport pandas as pd\nfrom math import inf\nfrom NearestNeighbor import *\nfrom scaling import *\n\n#Get and clean data\nsbff = pd.read_csv('SidiBelRegion.csv')\nsbff = sbff.drop(['day','year','month'],axis = 'columns')\nsbff = sbff.rename(columns ={' RH':'RH',' Ws':'Ws','Rain ':'Rain','Classes  ':'Classes'})\nnc = []\nfor i in sbff['Classes']:\n    if 'n' in i:\n        nc.append('not fire')\n    else:\n        nc.append('fire')\nsbff['Classes']=nc\n\n#Make feature dictionary\nsb ={}",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-sidibelsimilarityb-py",
      "title": "SidiBelSimilarityB",
      "section": "Machine Learning",
      "relative_path": "SidiBelSimilarityB.py",
      "summary": "In this project, I focus on sidiBel Similarity. I use pandas for tabular data handling.",
      "line_count": 34,
      "size_label": "0.8 KB",
      "modified": "2025-03-25T11:09:42.029138",
      "modified_label": "Mar 25, 2025",
      "file_url": "files/machine-learning/SidiBelSimilarityB.py",
      "preview": "#SidiBel Similarity\nimport pandas as pd\nfrom math import inf\nfrom NearestNeighbor import *\nfrom scalingFeatures import *\n\n#Get and clean data\nsbff = pd.read_csv('SidiBelRegion.csv')\nsbff = sbff.drop(['day','year','month'],axis = 'columns')\nsbff = sbff.rename(columns ={' RH':'RH',' Ws':'Ws','Rain ':'Rain','Classes  ':'Classes'})\nnc = []\nfor i in sbff['Classes']:\n    if 'n' in i:\n        nc.append('not fire')\n    else:\n        nc.append('fire')\nsbff['Classes']=nc\n\n#Make feature dictionary\nsb ={}",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-similaritynfldraft-py",
      "title": "similarityNFLDraft",
      "section": "Machine Learning",
      "relative_path": "similarityNFLDraft.py",
      "summary": "In this project, I focus on similarity Based Learning - NFL Draft. I implement functions such as feature, minkowskiDist, nearestNeighborNFL, and plotFeatureSpace. I create charts or visualizations and use NumPy for numeric computation. I render a chart or plotted output and read from local data files.",
      "line_count": 85,
      "size_label": "2.0 KB",
      "modified": "2025-03-12T11:54:03.746882",
      "modified_label": "Mar 12, 2025",
      "file_url": "files/machine-learning/similarityNFLDraft.py",
      "preview": "#Similarity Based Learning - NFL Draft\n\nimport numpy as np\nimport matplotlib.pyplot as plt\nfrom math import inf\n\n#Here is the feature space of the training data\n\n#takes a data file and turns it into a dictionary\ndef feature(featureDatafile, splitCh =','):\n    infile=open(featureDatafile,'r')\n   \n    feature={}\n    ID=1\n    for line in infile:\n        feature[ID]=line[:-1].split(splitCh)\n        ID+=1\n    infile.close()\n    return feature\n",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-stocktracker-py",
      "title": "stockTracker",
      "section": "Machine Learning",
      "relative_path": "stockTracker.py",
      "summary": "In this project, I focus on stock Tracker. I create charts or visualizations. I render a chart or plotted output and read from local data files. I read input from files like stockdata.txt. I can run this script directly to produce output or visual results.",
      "line_count": 48,
      "size_label": "1.1 KB",
      "modified": "2025-02-03T11:27:41.122267",
      "modified_label": "Feb 03, 2025",
      "file_url": "files/machine-learning/stockTracker.py",
      "preview": "#Stock Tracker\n\nimport matplotlib.pyplot as plt\n\ninfile = open('stockdata.txt','r')\ndata = {}\ninfile.readline()\nfor line in infile:\n    x = line.split('\\t')\n    date = x[0][:-5]\n    if len(date) == 3:\n        date = date[0]+date[1]+'0'+date[2]\n    \n    open_ = float(x[1])\n    high =float(x[2])\n    low = float(x[3])\n    close = float(x[4][:-1])\n    \n    data[date]=[open_,high,low, close]\n    ",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-studyguide-py",
      "title": "StudyGuide",
      "section": "Machine Learning",
      "relative_path": "StudyGuide.py",
      "summary": "In this file, I share part of my Machine Learning work. I include randomized behavior. I read from local data files. I read input from files like irisData2.txt. I can run this script directly to produce output or visual results.",
      "line_count": 37,
      "size_label": "0.5 KB",
      "modified": "2025-04-04T10:20:11.829731",
      "modified_label": "Apr 04, 2025",
      "file_url": "files/machine-learning/StudyGuide.py",
      "preview": "from NearestNeighbor import *\nfrom scalingFeature import *\nfrom evaluatingClassifiers import *\nfrom random import seed,randint\n\n\ninfile = open('irisData2.txt', 'r')\n\nirs = {}\nindex = 0\nfor line in infile:\n    ll = line[:-1].split(',')\n    irs[index] = ll\n    index += 1\n\ninfile.close()\n\n\nseed(10)\n",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-test-py",
      "title": "test",
      "section": "Machine Learning",
      "relative_path": "test.py",
      "summary": "In this file, I share part of my Machine Learning work. I define classes like Politician, Representative, and Senator. I implement functions such as __init__, __str__, collegial, and get_election_year. I build reusable functions.",
      "line_count": 77,
      "size_label": "2.5 KB",
      "modified": "2025-02-02T17:30:17.787030",
      "modified_label": "Feb 02, 2025",
      "file_url": "files/machine-learning/test.py",
      "preview": "from Guttag10 import Person     \n# Finger exercise from page 194\nclass Politician(Person):\n    \"\"\" A politician is a person that can belong to a political party\"\"\"\n    \n    def __init__(self, name, party = None):\n        \"\"\"name and party are strings\"\"\"\n        self.name = name\n        self.party = party\n        \n     #identifies partyName as the party or Independent if no party and returns the politician's Name and their party    \n    def __str__(self):\n        partyName = self.party if self.party else 'Independent'\n        return f'{self.name} ({partyName})'\n        \n  \n    def get_party(self):\n        \"\"\"returns the party to which self belongs\"\"\"\n        return self.party\n   ",
      "tags": [
        "Machine Learning",
        "Python"
      ]
    },
    {
      "id": "machine-learning-wineregression-py",
      "title": "wineRegression",
      "section": "Machine Learning",
      "relative_path": "wineRegression.py",
      "summary": "In this project, I focus on wine quality regression. I implement functions such as regrline. I use NumPy for numeric computation and use scikit-learn models and evaluation tools. I fit a linear regression model and read from local data files. I read input from files like winequality-red.txt.",
      "line_count": 29,
      "size_label": "0.7 KB",
      "modified": "2025-04-30T11:11:14.592811",
      "modified_label": "Apr 30, 2025",
      "file_url": "files/machine-learning/wineRegression.py",
      "preview": "#Wine quality regression\nimport numpy as np\nfrom sklearn.linear_model import LinearRegression\nfrom sklearn import metrics\nest = LinearRegression(fit_intercept = True)\nwinefile = open('winequality-red.txt','r')\n\nx=[]\ny=[]\nfor line in winefile:\n    lineList = line[:-1].split(';')\n    x.append([float(v) for v in lineList[:-1]])\n    y.append(float(lineList[-1]))\nwinefile.close()\nest.fit(x,y)\n\nprint(est.coef_,est.intercept_)\ndef regrline(coef,intc,x):\n    prod = 0\n    for i in range(len(coef)):",
      "tags": [
        "Machine Learning",
        "Python",
        "regression",
        "modeling"
      ]
    }
  ],
  "demos": [
    {
      "id": "demo-1",
      "title": "MU Performance Consulting AI Project Demo",
      "description": "Video walkthrough of the AI-powered project we have been working on with MU Performance Consulting this semester. Replace this description anytime with more project-specific details.",
      "status": "Coming soon",
      "project_url": "",
      "video_url": "",
      "thumbnail_url": "",
      "is_video": false,
      "has_thumbnail": false
    }
  ]
};

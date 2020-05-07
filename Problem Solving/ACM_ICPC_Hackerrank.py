def acmTeam(topics):
    m=len(topics)
    n=len(topics[0])
    ps=[]
    count=0
    each_knowledge_value_count={}
    maximum_knowledge=0
    for first_person in range(m):
        first_attendee=topic[first_person]
        for second_person in range(first_person+1,m):
            second_attendee=topic[second_person]
            for index in range(n):
                first_topic=first_attendee[index]
                second_topic=second_attendee[index]
                if not( first_topic == "0" and  second_topic == "0"):
                    count+=1
            maximum_knowledge=max(maximum_knowledge,count)
            if count not in each_knowledge_value_count:
                each_knowledge_value_count[count]=1
            else:
                each_knowledge_value_count[count]+=1
            count=0
    return [maximum_knowledge,each_knowledge_value_count[maximum_knowledge]]

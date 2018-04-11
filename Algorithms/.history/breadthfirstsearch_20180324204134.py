def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print person + ' is mango seller!!'
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

def person_is_seller(person):
    return name[-1] == 'm'


search("you")
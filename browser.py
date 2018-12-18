import webbrowser

q_list = ["광주날씨","광주미세먼지","길찾기"]

url ="https://www.google.com/search?q="

for q in q_list :
    webbrowser.open(url+q)
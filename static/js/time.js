// t2 = "8:00"
// t1 = "9:00"

// h1,s1 = t1.split(":")
// h2,s2 = t2.split(":")

// h = int(h2) - int(h1)
// s = int(s2) - int(s1)
// if h < 0:
// print(f"{24+h}:{s}")
//     if s < 0:
//     h -= 1
//     s = 0-s
    
//     f = f"{h}:{s}"
    
//     print(f)
function calculateHour(t2,t1) {
    t1 = t1.split(":")
    t2 = t2.split(":")
    h1 = t1[0]
    s1 = t1[1]

    h2 = t2[0]
    s2 = t2[1]

    h = Number(h2) - Number(h1)
    s = Number(s2) - Number(s1)
    if (h < 0) {
        return(24+h+":"+s);
    }
    if (s < 0) {
        h = h-1
        s = 60+s
    }
    return(h+":"+s) 
    
}
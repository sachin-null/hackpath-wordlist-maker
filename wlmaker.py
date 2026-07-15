#!/usr/bin/env python3
# ============================================================
#   HACKPATH WORDLIST MAKER v2
#   Created by: Sachin Ser | HackPath
#   Works on: Termux | Linux | Kali
#   Run: python3 wlmaker.py
#   No extra install needed — Pure Python!
#   GitHub: github.com/sachin-null/hackpath-wordlist-maker
# ============================================================

import os, sys, itertools

class C:
    R='\033[91m'; G='\033[92m'; Y='\033[93m'
    M='\033[95m'; CY='\033[96m'; W='\033[97m'
    DIM='\033[2m'; X='\033[0m'; B='\033[1m'

def clear(): os.system('clear' if os.name!='nt' else 'cls')

def banner():
    clear()
    print(C.G+C.B+"""
 __    __              _   _ _     _   
/ / /\ \ \___  _ __ __| | | (_)___| |_ 
\ \/  \/ / _ \| '__/ _` | | | / __| __|
 \  /\  / (_) | | | (_| | | | \__ \ |_ 
  \/  \/ \___/|_|  \__,_| |_|_|___/\__|                                                                                        """+C.Y+"""
                 _             
                | |            
 _ __ ___   __ _| | _____ _ __ 
| '_ ` _ \ / _` | |/ / _ \ '__|
| | | | | | (_| |   <  __/ |   
|_| |_| |_|\__,_|_|\_\___|_|                                                                                            
"""+C.X)
    print(C.CY+" +------------------------------------------+")
    print("  "+C.G+C.B+"WORDLIST MAKER v2"+C.CY+"  .  "+C.Y+"Sachin Ser"+C.CY+"     ")
    print("  "+C.DIM+"HackPath | Termux . Linux . Kali"+C.CY+"        ")
    print("  "+C.R+"Authorized / Educational use only!"+C.CY+"     ")
    print(" +------------------------------------------+"+C.X)
    print()

def sep(t=""):
    if t: print(f"\n{C.CY}{'='*14} {C.Y}{t}{C.CY} {'='*14}{C.X}")
    else: print(f"{C.DIM}{'-'*50}{C.X}")

def ok(m):    print(f"{C.G}[+] {m}{C.X}")
def err(m):   print(f"{C.R}[-] {m}{C.X}")
def inf(m):   print(f"{C.CY}[*] {m}{C.X}")
def fld(k,v): print(f"  {C.Y}{k:<20}{C.X}: {C.W}{v}{C.X}")
def pause():  input(f"\n{C.DIM}Press Enter...{C.X}")
def inp(p):   return input(f"{C.G}  {p} > {C.X}").strip()

# ── LEET SPEAK ──
def leet(w):
    t={'a':'@','e':'3','i':'1','o':'0',
       's':'$','t':'7','b':'8','g':'9','l':'1'}
    return ''.join(t.get(c,c) for c in w.lower())

# ── DATE VARIANTS ──
def date_vars(dob):
    v=set()
    d=dob.strip().replace('-','').replace('/','') \
         .replace('.','').replace(' ','')
    if not d: return v
    v.add(d)
    if len(d)==8:
        dd,mm,yy4,yy2=d[:2],d[2:4],d[4:],d[6:]
        v.update([
            dd+mm+yy4, mm+dd+yy4, yy4+mm+dd,
            dd+mm+yy2, mm+dd+yy2,
            dd+mm, mm+dd, yy4, yy2,
            dd+mm+yy4+'!', yy4+'!', yy2+'!',
            dd+mm+yy4+'@', dd+mm+yy2+'@',
            dd+mm+yy4+'#', yy4+'786',
        ])
    elif len(d)==6:
        dd,mm,yy=d[:2],d[2:4],d[4:]
        v.update([dd+mm+yy,mm+dd+yy,dd+mm,yy,
                  dd+mm+yy+'!',yy+'!'])
    elif len(d)==4:
        v.update([d,d[2:],d+'!',d+'@',d+'786'])
    return v

# ── MUTATIONS ──
def mutate(word):
    v=set()
    w=word.strip()
    if not w: return v

    suffs=[
        '1','12','123','1234','12345','123456',
        '!','@','#','$','!!','@123','786','007',
        '999','111','000','2024','2025','2026','2023',
        '1!','12!','123!','_1','_123','_786',
        '01','001','007!','786!','@2024','@2025',
        '123!','1234!','#786','*123',
    ]
    prefs=['1','12','123','@','my','mr','ms','the','']

    # Basic variants
    v.update([w,w.lower(),w.upper(),w.capitalize()])
    # Leet
    v.update([leet(w),leet(w).capitalize(),
               leet(w).upper()])
    # Reverse
    v.update([w[::-1],w.lower()[::-1]])
    # Double
    v.add(w.lower()+w.lower())
    v.add(w.capitalize()+w.lower())
    v.add(w.lower()+w.capitalize())

    # With suffixes
    for s in suffs:
        v.update([
            w+s, w.lower()+s,
            w.capitalize()+s,
            leet(w)+s,
            w.upper()+s,
        ])
    # With prefixes
    for p in prefs:
        if p:
            v.update([p+w,p+w.capitalize(),
                      p+w.lower()])
    return v

# ══════════════════════════════════════════
#   1. FULL WORDLIST GENERATOR
# ══════════════════════════════════════════
def generate():
    sep("FULL WORDLIST GENERATOR")
    print(f"{C.DIM}  Leave blank to skip any field{C.X}\n")

    print(C.Y+"── PERSONAL ──"+C.X)
    name    = inp("Full Name / Username")
    dob     = inp("Birthday (ddmmyyyy)")
    phone   = inp("Phone number")

    print(C.Y+"\n── EXTRA ──"+C.X)
    pet     = inp("Pet / Nickname")
    partner = inp("Partner name")
    city    = inp("City / Hometown")
    keyword = inp("Keyword / Interest")
    fav     = inp("Favourite number")
    company = inp("Company / School")

    print(C.Y+"\n── OUTPUT ──"+C.X)
    fname   = inp(f"Output file [{C.G}wordlist.txt{C.X}]") or "wordlist.txt"
    try:
        minl = int(inp(f"Min length [{C.G}4{C.X}]") or "4")
        maxl = int(inp(f"Max length [{C.G}20{C.X}]") or "20")
    except:
        minl,maxl=4,20

    inf("Generating wordlist...")
    wl=set()

    # Collect base words
    bases=[x for x in [name,pet,partner,city,keyword,company] if x]

    # Split name into parts
    if name:
        parts=name.split()
        bases.extend(parts)
        if len(parts)>=2:
            bases.append(parts[0]+parts[-1])
            bases.append(parts[-1]+parts[0])
            bases.append(parts[0][0]+parts[-1])
            bases.append(parts[0]+parts[-1][0])
            bases.append(parts[0][:3]+parts[-1][:3])

    # Mutate each base
    for b in bases:
        wl.update(mutate(b))

    # Date variants
    dv=date_vars(dob)
    wl.update(dv)

    # Phone variants
    if phone:
        p=phone.replace(' ','').replace('-','') \
               .replace('+','').replace('(','').replace(')','')
        for sl in [p,p[-10:],p[-8:],p[-6:],p[-4:]]:
            if sl:
                wl.add(sl)
                for b in bases[:4]:
                    wl.add(b.lower()+sl)
                    wl.add(b.capitalize()+sl)
                    wl.add(sl+b.lower())

    # Favourite number
    if fav:
        wl.add(fav)
        for b in bases:
            wl.add(b+fav)
            wl.add(b.capitalize()+fav)
            wl.add(fav+b.lower())
            wl.add(b.lower()+fav+'!')
            wl.add(b.lower()+fav+'@')

    # Base + date combos
    for b in bases:
        for d in dv:
            wl.update([
                b.lower()+d, b.capitalize()+d,
                b.lower()+d+'!', b.lower()+d+'@',
                b+d+'786', b+d+'123', b+d+'#',
                b.upper()+d,
            ])

    # Base combinations
    for b1,b2 in itertools.permutations(bases[:6],2):
        wl.update([
            b1.lower()+b2.lower(),
            b1.capitalize()+b2.capitalize(),
            b1.capitalize()+b2.lower(),
            b1+'_'+b2, b1+'.'+b2,
            b1+b2+'123', b1+b2+'!',
            b1+b2+'@', b1+b2+'786',
            b1+'@'+b2, b1+'#'+b2,
        ])

    # Common patterns
    commons=[
        '123','1234','12345','123456','password',
        'pass','admin','786','007','999','love',
        'dear','star','king','queen','hero','god',
        'cool','best','super','2024','2025',
    ]
    for b in bases[:5]:
        for c in commons:
            wl.update([b.lower()+c,b.capitalize()+c,
                       c+b.lower(),b.lower()+c+'!'])

    # Filter
    wl={w for w in wl if minl<=len(w)<=maxl and w.strip()}
    final=sorted(wl)

    # Save
    with open(fname,'w',encoding='utf-8') as f:
        for w in final: f.write(w+'\n')

    sep("RESULT")
    ok(f"Generated {C.Y}{len(final):,}{C.G} unique passwords!")
    ok(f"Saved  →  {C.Y}{fname}")
    fld("Min/Max length",f"{minl} / {maxl}")
    fld("Base words",str(len(bases)))

    print(f"\n{C.CY}  Preview (first 15):{C.X}")
    for w in final[:15]:
        print(f"  {C.W}{w}{C.X}")
    if len(final)>15:
        print(f"  {C.DIM}... and {len(final)-15:,} more{C.X}")

    print(f"""
{C.Y}  Use with:{C.X}
  {C.G}hydra{C.X}   -L users.txt -P {fname} ssh://target
  {C.G}john{C.X}    --wordlist={fname} hash.txt
  {C.G}hashcat{C.X} -a 0 -m 0 hash.txt {fname}

  {C.DIM}by Sachin Ser | HackPath{C.X}
""")
    pause()

# ══════════════════════════════════════════
#   2. QUICK MODE
# ══════════════════════════════════════════
def quick():
    sep("QUICK MODE")
    name  = inp("Name / Username")
    dob   = inp("Birthday (ddmmyyyy)")
    extra = inp("Extra word (pet/city/keyword)")
    fname = inp(f"Output [{C.G}quick.txt{C.X}]") or "quick.txt"

    wl=set()
    bases=[x for x in [name,extra]+name.split() if x]
    for b in bases:
        wl.update(mutate(b))
    dv=date_vars(dob)
    wl.update(dv)
    for b in bases:
        for d in dv:
            wl.update([b.lower()+d,b.capitalize()+d,
                       b.lower()+d+'!',b+d+'@'])

    wl={w for w in wl if 4<=len(w)<=20}
    final=sorted(wl)
    with open(fname,'w') as f:
        for w in final: f.write(w+'\n')

    ok(f"{len(final):,} passwords → {fname}")
    for w in final[:10]:
        print(f"  {C.W}{w}{C.X}")
    pause()

# ══════════════════════════════════════════
#   3. KEYWORD WORDLIST
# ══════════════════════════════════════════
def keyword_list():
    sep("KEYWORD WORDLIST")
    print(f"{C.DIM}  Generate from multiple keywords{C.X}\n")

    keywords=[]
    inf("Enter keywords (empty line to stop):")
    while True:
        k=inp(f"Keyword {len(keywords)+1}")
        if not k: break
        keywords.append(k)

    if not keywords:
        err("No keywords!"); pause(); return

    fname = inp(f"Output [{C.G}keywords.txt{C.X}]") or "keywords.txt"
    try:
        minl=int(inp("Min length [4]") or "4")
        maxl=int(inp("Max length [20]") or "20")
    except: minl,maxl=4,20

    wl=set()
    for kw in keywords:
        wl.update(mutate(kw))

    # Combinations
    for k1,k2 in itertools.permutations(keywords[:6],2):
        wl.update([
            k1.lower()+k2.lower(),
            k1.capitalize()+k2,
            k1+'_'+k2, k1+'.'+k2,
            k1+k2+'123', k1+k2+'!',
        ])

    wl={w for w in wl if minl<=len(w)<=maxl}
    final=sorted(wl)
    with open(fname,'w') as f:
        for w in final: f.write(w+'\n')

    ok(f"{len(final):,} passwords from {len(keywords)} keywords → {fname}")
    pause()

# ══════════════════════════════════════════
#   4. COMBINE WORDLISTS
# ══════════════════════════════════════════
def combine_lists():
    sep("COMBINE WORDLISTS")
    print(f"{C.DIM}  Merge multiple wordlist files{C.X}\n")

    files=[]
    inf("Enter file names (empty to stop):")
    while True:
        f=inp(f"File {len(files)+1}")
        if not f: break
        if os.path.exists(f):
            files.append(f)
            ok(f"Added: {f}")
        else:
            err(f"File not found: {f}")

    if not files:
        err("No files!"); pause(); return

    fname=inp("Output file [combined.txt]") or "combined.txt"
    dedup=inp("Remove duplicates? [Y/n]").lower()!='n'

    all_words=[]
    for f in files:
        with open(f,'r',errors='ignore') as fp:
            words=[l.strip() for l in fp if l.strip()]
            all_words.extend(words)
            inf(f"{f}: {len(words):,} words")

    if dedup:
        all_words=sorted(set(all_words))

    with open(fname,'w') as fp:
        for w in all_words: fp.write(w+'\n')

    ok(f"Combined {len(all_words):,} words → {fname}")
    pause()

# ══════════════════════════════════════════
#   5. WORDLIST FILTER
# ══════════════════════════════════════════
def filter_list():
    sep("WORDLIST FILTER")
    fname=inp("Input wordlist file")
    if not fname or not os.path.exists(fname):
        err("File not found!"); pause(); return

    with open(fname,'r',errors='ignore') as f:
        words=[l.strip() for l in f if l.strip()]
    inf(f"Loaded {len(words):,} words")

    print(f"\n  Filters:")
    try:
        minl=int(inp("Min length [0]") or "0")
        maxl=int(inp("Max length [100]") or "100")
    except: minl,maxl=0,100

    has_upper=inp("Must have uppercase? [y/N]").lower()=='y'
    has_lower=inp("Must have lowercase? [y/N]").lower()=='y'
    has_digit=inp("Must have digit? [y/N]").lower()=='y'
    has_spec =inp("Must have special? [y/N]").lower()=='y'
    contains =inp("Must contain (leave blank to skip)") or ""

    import re
    filtered=[]
    for w in words:
        if not (minl<=len(w)<=maxl): continue
        if has_upper and not re.search(r'[A-Z]',w): continue
        if has_lower and not re.search(r'[a-z]',w): continue
        if has_digit and not re.search(r'\d',w): continue
        if has_spec  and not re.search(r'[^a-zA-Z0-9]',w): continue
        if contains  and contains.lower() not in w.lower(): continue
        filtered.append(w)

    outfile=inp("Output file [filtered.txt]") or "filtered.txt"
    with open(outfile,'w') as f:
        for w in filtered: f.write(w+'\n')

    ok(f"Filtered: {len(words):,} → {len(filtered):,} words → {outfile}")
    fld("Removed",str(len(words)-len(filtered)))
    pause()

# ══════════════════════════════════════════
#   6. WORDLIST STATS
# ══════════════════════════════════════════
def wordlist_stats():
    sep("WORDLIST STATISTICS")
    fname=inp("Wordlist file")
    if not fname or not os.path.exists(fname):
        err("File not found!"); pause(); return

    with open(fname,'r',errors='ignore') as f:
        words=[l.strip() for l in f if l.strip()]

    if not words:
        err("Empty file!"); pause(); return

    import re
    lengths=[len(w) for w in words]

    sep("STATS")
    fld("Total words",    f"{len(words):,}")
    fld("Unique words",   f"{len(set(words)):,}")
    fld("Duplicates",     f"{len(words)-len(set(words)):,}")
    fld("Min length",     str(min(lengths)))
    fld("Max length",     str(max(lengths)))
    fld("Avg length",     f"{sum(lengths)/len(lengths):.1f}")
    fld("File size",      f"{os.path.getsize(fname)/1024:.1f} KB")

    sep("CHARSET ANALYSIS")
    has_u=sum(1 for w in words if re.search(r'[A-Z]',w))
    has_l=sum(1 for w in words if re.search(r'[a-z]',w))
    has_d=sum(1 for w in words if re.search(r'\d',w))
    has_s=sum(1 for w in words if re.search(r'[^a-zA-Z0-9]',w))
    fld("With uppercase",f"{has_u:,} ({has_u*100//len(words)}%)")
    fld("With lowercase",f"{has_l:,} ({has_l*100//len(words)}%)")
    fld("With digits",   f"{has_d:,} ({has_d*100//len(words)}%)")
    fld("With special",  f"{has_s:,} ({has_s*100//len(words)}%)")

    sep("LENGTH DISTRIBUTION")
    from collections import Counter
    dist=Counter(lengths)
    for l in sorted(dist.keys())[:10]:
        bar='█'*min(dist[l]*30//max(dist.values()),30)
        print(f"  {C.Y}{l:<4}{C.X} {C.G}{bar}{C.X} {dist[l]:,}")
    pause()

# ══════════════════════════════════════════
#   MAIN MENU
# ══════════════════════════════════════════
def main():
    while True:
        banner()
        print(f"  {C.B}MENU{C.X}")
        print(f"  {C.G}[1]{C.X} Full Wordlist      (all personal info)")
        print(f"  {C.G}[2]{C.X} Quick Mode          (name + birthday)")
        print(f"  {C.G}[3]{C.X} Keyword Wordlist    (multiple keywords)")
        print(f"  {C.G}[4]{C.X} Combine Wordlists   (merge files)")
        print(f"  {C.G}[5]{C.X} Filter Wordlist     (by length/charset)")
        print(f"  {C.G}[6]{C.X} Wordlist Stats      (analyze file)")
        print(f"  {C.R}[0]{C.X} Exit")
        print(f"\n{C.DIM}  python3 wlmaker.py | HackPath v2{C.X}\n")

        ch=input(f"{C.G}HackPath WL > {C.X}").strip()

        menu={
            '1':generate,'2':quick,'3':keyword_list,
            '4':combine_lists,'5':filter_list,'6':wordlist_stats,
        }

        if ch in menu: menu[ch]()
        elif ch=='0':
            print(f"\n{C.G}Bye! 👋{C.X}\n"); sys.exit(0)
        else:
            print(f"{C.R}Invalid!{C.X}")

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{C.G}Bye! 👋{C.X}\n")
        sys.exit(0)

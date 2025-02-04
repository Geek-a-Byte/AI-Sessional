# -*- coding: utf-8 -*-
"""Mancala Assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10A2LphAKazbSHRWlXDLzJcpoAm4v1Tlm
"""

human_list =    [0,4,4,4,4,4,4,0];
computer_list = [0,4,4,4,4,4,4,0];
fix_lvl = 5;

def h1(h,c):
    sum1=0; # for computer_list
    sum2=0; # for human_list
    for i in range(1,7):
        sum2+=h[i];
    for i in range(1,7):
        sum1+=c[i];
    if(c[7]>=h[0] and sum1<=sum2):
        return c[7]+sum1;
    return c[0];

def h2(h,c):
    sum1=0; # for computer_list
    sum2=0; # for human_list
    for i in range(1,7):
        sum2+=h[i];
    for i in range(1,7):
        sum1+=c[i];
    if(c[7]<=h[0] and sum1>=sum2):
        return h[0]+sum2;
    return h[0];

## human array = [ 0 1 2 3 4 5 6 7] /// 0 is store box
## AI array =    [ 0 1 2 3 4 5 6 7] /// 7 is store box

def call(h,c,pit_no,whos_turn):
    print_list(h, c);
    # computer turn
    if(whos_turn == 0):
        whos_pit = 0; # to track where the last stone falls
        stone = c[pit_no];
        c[pit_no] = 0;
        
        while(stone>0):
            if(whos_pit==0):
                pit_no+=1;
                if(pit_no>7):
                    whos_pit = 1;
                    pit_no=6;
            else:
                pit_no-=1;
                if(pit_no<=0):
                    whos_pit = 0;
                    pit_no=1;
            
            if(stone!=1):
                if(whos_pit==0):
                    c[pit_no]+=1;
                else:
                    h[pit_no]+=1;
            else:
                if(whos_pit==1):
                    h[pit_no]+=1;
                else:
                    if(pit_no==7):
                        c[pit_no]+=1;
                        return True; #return true means computer will get an extra move now
                    elif(c[pit_no]==0):
                        if(h[pit_no]):
                            c[7]+=1+h[pit_no];
                            h[pit_no]=0;
                        else:
                            c[pit_no]+=1;
                    else:
                        c[pit_no]+=1;
            stone-=1;
    # human turn
    else:
        whos_pit = 1;
        stone = h[pit_no];
        h[pit_no] = 0;
        
        while(stone>0):
            if(whos_pit==0):
                pit_no+=1;
                if(pit_no>=7):
                    whos_pit = 1;
                    pit_no=6;
            else:
                pit_no-=1;
                if(pit_no<0):
                    whos_pit = 0;
                    pit_no=1;
            
            if(stone!=1):
                if(whos_pit==0):
                    c[pit_no]+=1;
                else:
                    h[pit_no]+=1;
            else:
                if(whos_pit==0):
                    c[pit_no]+=1;
                else:
                    if(pit_no==0):
                        h[pit_no]+=1;
                        return True; #return true means human gets an extra move
                    elif(h[pit_no]==0):
                        if(c[pit_no]):
                            h[0]+=1+c[pit_no];
                            c[pit_no]=0;
                        else:
                            h[pit_no]+=1;
                    else:
                        h[pit_no]+=1;
            stone-=1;

    return False;


def goalTest(h,c):
    sum1=0;
    sum2=0;
    for i in range(1,7):
        sum2+=h[i];
    for i in range(1,7):
        sum1+=c[i];
        
    if(sum1==0 or sum2==0):
        return True;
    else:
        return False;
    
def max_value(h,c,alpha,beta,lvl):
    if(goalTest(h,c)):
        return -c[7];
    if(lvl==0):
        return -h1(h,c);
    
    idx = 0;
    for i in range(1,7):
        if(c[i]==0):
            continue;
        temp_c = c;
        temp_h = h;
        while(1):
            if(goalTest(temp_h,temp_c)==True):
                break;
            if(call(temp_h,temp_c,i,0)==False):
                break;
        print("after while");
        ans_min=min_value(temp_h,temp_c,alpha,beta,lvl-1);
        if(beta!=0):
            if(ans_min>=beta):
                return 1000000000;
        if(alpha==0):
            alpha=ans_min;
        if(ans_min>=alpha):
            idx=i;
            alpha=ans_min;
    if(lvl==fix_lvl):
        return idx;
    return alpha;

def min_value(h,c,alpha,beta,lvl):
    if(goalTest(h,c)):
        return c[7];
    if(lvl==0):
        return h2(h,c);
    
    for i in range(1,7):
        if(h[i]==0):
            continue;
        temp_c = c;
        temp_h = h;
        while(1):
            if(goalTest(temp_h,temp_c)):
                break;
            if(call(temp_h,temp_c,i,1)==False):
                break;
        ans_max=max_value(temp_h,temp_c,alpha,beta,lvl-1);
        if(alpha!=0):
            if(ans_max<=alpha):
                return -ans_max;
        if(beta==0):
            beta=ans_max;
        beta=min(beta,ans_max);
    return beta;

def print_list(h,c):
    print('\n',end=' ');
    for i in range(1,7):
        print(h[i],end=' ');
    print("         <-----Human");
    print(h[0],end='           ')
    print(c[7]);
    print(end=' ');
    for i in range(1,7):
        print(c[i],end=' ');
    print("         <-----Computer");
    print('\n\n');

print ("\n----------Mancala using Alpha-Beta Pruning--------\n");

whos_turn = 0; 
# whos_turn -> 0 means human
# whos_turn -> 1 means computer

print_list(human_list, computer_list);

while(goalTest(human_list,computer_list) == False):
    # humans' turn
    print(whos_turn,end="\n");
    if(whos_turn==0):
        print("Human's turn");
        which_pit = int(input('Human Turns choose(1-6): '));
        if(human_list[which_pit]):
            extra_turn_or_not = call(human_list,computer_list,which_pit, 1);
            print_list(human_list, computer_list);
            if(extra_turn_or_not == False): 
                whos_turn^=1;
        else:
            print('Invalid choice\n');
    else:
        print('Computer Chose: ');
        d = max_value(human_list,computer_list,0,0,fix_lvl);
        print(d,end='\n');
        extra_turn= call(human_list,computer_list,d, 0);
        print_list(human_list, computer_list);
        if(extra_turn == False): 
            whos_turn^=1;

for i in range(1,7):
    computer_list[7] += computer_list[i];

for i in range(1,7):
    human_list[0] += human_list[i];

if(computer_list[7]>human_list[0]):
    print('\n\n____________Computer wins__________\n\n');
elif(computer_list[7] == human_list[0]):
    print('\n\n____________Game Draw__________\n\n');
else:
    print('\n\n____________Human Wins__________\n\n');
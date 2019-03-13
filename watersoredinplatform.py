def WaterStoredInPlatform(platform):
    def check_block_valid(x,y,a_matrix,platform,main_list,diff_val):
        #if x <=a_matrix.shape[0]
        #ret_val ='N'
        #diff_val=value_block
        #print('call')
        valid_flag ='N'
        key_values=[(0,-1),(0,1),(-1,0),(1,0)]
        if x==a_matrix.shape[0]-1 or y==a_matrix.shape[1]-1 or x==0 or y==0:
            main_list =[]
            #print('last line','x-',x,'y-',y)
            return 0
        for index in key_values:
            gap_present=False
            l=x+index[0]
            m=y+index[1]
            #print('in loop--',l,',',m,'x-y',x,'-',y)
            if (a_matrix[x][y] < a_matrix[l][m] or (l,m) in main_list):
                #print('diff_valnaveen',a_matrix[l][m]-a_matrix[x][y])
                if diff_val >a_matrix[l][m] - a_matrix[x][y] and a_matrix[x][y] < a_matrix[l][m]:
                    diff_val =a_matrix[l][m] - a_matrix[x][y]
                if platform[x][y]==0:
                    gap_present=True
                
            else:
                #print('1','else',main_list)
                main_list.append((x,y))
                if platform[x][y]==0:
                    gap_present=True
                #print('diff_val',diff_val,'x-',x,'y-',y,'l-',l,'m-',m)
                diff_val=check_block_valid(l,m,a_matrix,platform,main_list,diff_val)
                #print(diff_val)
            if gap_present:
                diff_val=0
        if diff_val==0:
            main_list=[]
        #print('main_list',main_list)
        return diff_val
    stor_list=[]
    rows=platform.shape[0]
    columns=platform.shape[1]
    area=0
    i=0
    end_loop = False
    total_area=0
    a_matrix=platform
    while(end_loop == False):
        #print('naveen the king')
        total_area+=area
        i=0
        while (i <rows):
            j=0
            while(j<columns):
                #print((i,j))
                if check_block_valid(i,j,a_matrix,platform,[],np.max(a_matrix)+1)>0 and a_matrix[i][j]==0:
                    area=area+1
                    #print(i,j)
                j=j+1
            i=i+1
        #print(a_matrix)
        #print(area)
        a_matrix=a_matrix-1
        a_matrix[a_matrix <0]=0
        if np.max(a_matrix)==0:
            end_loop=True
    return area

def main():
    S = input().lower()
    if 1 <= len(S) <= 1000:

        n = len(S) 
        tam = -1

        for i in range(n):
            for j in range(i + 1, n):
                sub_string = S[i:j]
                if S.count(sub_string) > 1:
                    tam = max(tam, S.rindex(sub_string) - S.index(sub_string) + len(sub_string))
        print(tam)
       
if __name__ == "__main__":
    main()

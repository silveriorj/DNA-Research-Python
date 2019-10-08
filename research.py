#     FAMILY
fam_aa = "AACGTCT"  
fam_tc = "TCGACGG"  
fam_cc = "CCTTGAA"  
#     GENRE
gen_tt = "TTAACGC"
gen_gg = "GGATACC" 
gen_cg = "CGCGTTA"
#     Archives
catalog, albina, cicada, scorpion = "catalogo.txt", "albina.txt", "cigarra.txt", "escorpiao.txt"

def search (arq):
    a, b, c, d, e, f = 0, 0, 0, 0, 0, 0
    with open(arq, "r") as file:
        print("\033[35m[INFO] Extracting the {"+arq+"} data...\033[0;0m")
        for line in file:
            line.replace('\n', '')
            # Reading the FAMILY DNA codes
            if line.find(fam_aa) != -1:
                a = a+1
            if line.find(fam_tc) != -1:
                b = b+1
            if line.find(fam_cc) != -1:
                c = c+1
            # Reading the GENRE DNA codes
            if line.find(gen_tt) != -1:
                d = d+1
            if line.find(gen_gg) != -1:
                e = e+1
            if line.find(gen_cg) != -1:
                f = f+1
    file.close()
    print("\033[36m[CHECKPOINT] Extraction completed!\033[0;0m")
    return a,b,c,d,e,f

def saveFile(alb_a, alb_b, alb_c, alb_d, alb_e, alb_f, cic_a, cic_b, cic_c, cic_d, cic_e, cic_f,
            sco_a, sco_b, sco_c, sco_d, sco_e, sco_f):
    print("\033[35m[INFO] Saving data...")

    if open(catalog, "w"):
        file = open(catalog,"w")

        cat = "ARANHA ALBINA\n(Theridiidae / Phoneutria)\n\nSequências - Familia\t\tSequências - Gênero\n"
        cat = cat+"[AACGTCT]: "+str(alb_a)+" vezes\t\t\t[TTAACGC]: "+str(alb_d)+" vezes\n"
        cat = cat+"[TCGACGG]: "+str(alb_b)+" vezes\t\t\t[GGATACC]: "+str(alb_e)+" vezes\n"
        cat = cat+"[CCTTGAA]: "+str(alb_c)+" vezes\t\t\t[CGCGTTA]: "+str(alb_f)+" vezes\n"
        
        cat = cat+"\n\nARANHA CIGARRA\n(Theridiidae /  Avicularia)\n\nSequências - Familia\t\tSequências - Gênero\n"
        cat = cat+"[AACGTCT]: "+str(cic_a)+" vezes\t\t\t[TTAACGC]: "+str(cic_d)+" vezes\n"
        cat = cat+"[TCGACGG]: "+str(cic_b)+" vezes\t\t\t[GGATACC]: "+str(cic_e)+" vezes\n"
        cat = cat+"[CCTTGAA]: "+str(cic_c)+" vezes\t\t\t[CGCGTTA]: "+str(cic_f)+" vezes\n"
        
        cat = cat+"\n\nARANHA ESCORPIÃO\n(Theraphosidae  /  Latrodectus)\n\nSequências - Familia\t\tSequências - Gênero\n"
        cat = cat+"[AACGTCT]: "+str(sco_a)+" vezes\t\t\t[TTAACGC]: "+str(sco_d)+" vezes\n"
        cat = cat+"[TCGACGG]: "+str(sco_b)+" vezes\t\t\t[GGATACC]: "+str(sco_e)+" vezes\n"
        cat = cat+"[CCTTGAA]: "+str(sco_c)+" vezes\t\t\t[CGCGTTA]: "+str(sco_f)+" vezes\n"

        file.write(cat)
        file.close()

        print("\033[32m[FINISH] The data was saved and the program has ended.")
    else:
        print("\033[31m[ERRO] Falha ao Salvar Informações!\n")        


print("\033[33m[BEGIN] Starting the extraction...")
alb_a, alb_b, alb_c, alb_d, alb_e, alb_f = search(albina)
cic_a, cic_b, cic_c, cic_d, cic_e, cic_f = search(cicada)
sco_a, sco_b, sco_c, sco_d, sco_e, sco_f = search(scorpion)
saveFile(alb_a, alb_b, alb_c, alb_d, alb_e, alb_f, cic_a, cic_b, cic_c, cic_d, cic_e, cic_f,
    sco_a, sco_b, sco_c, sco_d, sco_e, sco_f)
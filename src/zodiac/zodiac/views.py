# -*- coding: utf-8 -*-
import random
def root_view(request):
    #array dimatges
    imatges = ['1_aries.jpg','2_tauro.jpg','3_geminis.jpg','4_cancer.jpg','5_leo.jpg','6_virgo.jpg','7_libra.jpg','8_escorpi.jpg','9_sagitari.jpg','10_capricorn.jpg','11_aquari.jpg','12_piscis.jpg']
    #clau imatges valor variable imatges i va sense cometes pk no vui pasar un string sino  una variable al return
    
    return {'project':'zodiac','imatges':imatges}
def elmeu_view(request):
    
    if request.method=="POST":
        
        frases=["Demà tindràs un día agradable, no cometis cap error i seràs recompensat.","Demà pot ser que et toqui la loteria...pensa-hi.","Pot ser que en algun moment del dia, algú et saludi, torna-li el saludo efusivament i seràs recompensat.","Vigila amb els actes que comets, perjudicaran a terceres persones... ","Vés al metge, crec que ja es hora de que facis alguna revisió de tan en tan. ","Si menges fruits secs sovints, poc esforç mental hauràs de fer en els examens ",]
        num=random.randint(0,5)#num aleatori amb random per a que escolleixi frase
        imatges = ['10_capricorn.jpg','11_aquari.jpg','12_piscis.jpg','1_aries.jpg','2_tauro.jpg','3_geminis.jpg','4_cancer.jpg','5_leo.jpg','6_virgo.jpg','7_libra.jpg','8_escorpi.jpg','9_sagitari.jpg']
        #imatges = ['1_aries.jpg','2_tauro.jpg','3_geminis.jpg','4_cancer.jpg','5_leo.jpg','6_virgo.jpg','7_libra.jpg','8_escorpi.jpg','9_sagitari.jpg','10_capricorn.jpg','11_aquari.jpg','12_piscis.jpg']
        dia=request.POST.get("dia")
        mes=request.POST.get('mes')
        nom=request.POST.get('nom')
        ano=request.POST.get('any')
        mesos = ['Gener','Febrer','Març','Abril','Maig','Juny','Juliol','Agost','Setembre','Octubre','Novembre','Desembre']
        frase=frases[num].decode('utf-8')# decode per a que accepti els accents
        lletres_mes=mesos[int(mes)]
        num_mes=int(mes)+1
        signes = ['Capricorn','Aquari','Peixos', 'Àries','Taure', 'Bessons', 'Càncer', 'Lleó', 'Verge', 'Balança', 'Escorpí', 'Sagitari']
        #signes = ['Àries','Taure','Bessons','Càncer','Lleó','Verge','Balança','Escorpí','Sagitari','Capricorn','Aquari','Peixos']
        #dies_finals_signes = [20,21,21,22,22,22,22,22,21,20,19,20]
        dies_finals_signes = [20,19,20,20,21,21,22,22,22,22,22,21]
        # 21/03 - 20/04  21/04 - 21/05    22/05 - 21/06  22/06 - 22/07 23/07 - 22/08  23/08 - 22/09  23/09 - 22/10 23/10 - 22/11 23/11 - 21/12   22/12 - 20/01   21/01 - 19/02   20/02 - 20/03
        #22/12 - 20/01   21/01 - 19/02  20/02 - 20/03  21/03 - 20/04 21/04 - 21/05    22/05 - 21/06  22/06 - 22/07 23/07 - 22/08  23/08 - 22/09  23/09 - 22/10 23/10 - 22/11 23/11 - 21/12
        #signe=signes[dies_finals_signes]
        
        
       # if dia >= 21 and mes == 2:
        #   signes[0]
        #   if dia <= 20 and mes == 3:
        #       signes[0]
        dia=int(dia)
        mes=int(mes)
       # extret de : http://geekytheory.com/calcula-tu-zodiaco-con-python/
        if dia > dies_finals_signes[int(mes)]:
            mes=mes+1
        if mes==12:
            mes=0
        #
        imatge_signe=imatges[int(mes)].decode('utf-8')
        signe=signes[int(mes)].decode('utf-8')
        """if dia >= 21 and mes == 2  or dia <= 20 and mes == 3:
            signes[0]
            imatges[0]
        if dia >= 21 and mes == 3  or dia <= 21 and mes == 4:
            a=signes[1]
            b=imatges[1]
            
        if mes == 2: #març
            if dia > 20:
                signes[0] #aries
                #return "Aries"
            else:
                signes[11] #peixos
                #return "Peixos"
                
        elif mes == 3: #abril
            if dia > 20:
                signes[
                return "Taure"
            else:
                return "Aries"""

        return {"dia":dia,"mes":mes,"nom":nom,"ano":ano,"lletres_mes":lletres_mes,"frase":frase,"num_mes":num_mes,"signe":signe,"imatge_signe":imatge_signe,'project':'zodiac'}
            
    
    return {'project':'zodiac'}
    

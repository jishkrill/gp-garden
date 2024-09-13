import re

# (Fill in your actual data here)
data = """
## Practice
    
    [Venous eczema and chronic venous disease](https://www.bmj.com/content/382/bmj-2022-074602)
    
    Published 17 August 2023
    
## Practice
    
    [HIV prevention with postexposure prophylaxis-in-pocket (PIP)](https://www.bmj.com/content/382/bmj-2023-076016)
    
    Published 02 August 2023
    
## Practice
    
    [Can I have blood tests to check everything is alright?](https://www.bmj.com/content/382/bmj-2023-075728)
    
    Published 05 July 2023
    
## Practice
    
    [Gynaecomastia](https://www.bmj.com/content/379/bmj-2021-069771)
    
    Published 20 October 2022
    
## Practice
    
    [Visible haematuria](https://www.bmj.com/content/376/bmj-2021-067395)
    
    Published 01 February 2022
    
## Practice
    
    [Chronic anal fissure in adults](https://www.bmj.com/content/376/bmj-2021-066834)
    
    Published 12 January 2022

  

 

## Practice
    
    [Primary herpetic gingivostomatitis in children](https://www.bmj.com/content/375/bmj-2021-065540)
    
    Published 31 December 2021
    
## Practice
    
    [Childhood constipation](https://www.bmj.com/content/375/bmj-2021-065046)
    
    Published 02 December 2021
    
## Practice
    
    [Overactive bladder in women](https://www.bmj.com/content/375/bmj-2020-063526)
    
    Published 01 December 2021
    
## Practice
    
    [Biliary colic](https://www.bmj.com/content/374/bmj.n2085)
    
    Published 13 September 2021
    
## Practice
    
    [Virtual consultation for red eye](https://www.bmj.com/content/373/bmj.n1490)
    
    Published 25 June 2021
    
## Practice
    
    [Otitis externa](https://www.bmj.com/content/372/bmj.n714)
    
    Published 31 March 2021
  

 

## Practice
    
    [Uncomplicated urinary tract infection in women](https://www.bmj.com/content/372/bmj.n725)
    
    Published 30 March 2021
    
## Practice
    
    [What is my covid risk?](https://www.bmj.com/content/372/bmj.n637)
    
    Published 16 March 2021
    
## Practice
    
    [A lump in the throat: laryngopharyngeal reflux](https://www.bmj.com/content/371/bmj.m4091)
    
    Published 02 November 2020
    
## Practice
    
    [Forefoot pain](https://www.bmj.com/content/371/bmj.m3704)
    
    Published 09 October 2020
    
## Practice
    
    [Growth concerns in the early weeks of life](https://www.bmj.com/content/370/bmj.m3533)
    
    Published 21 September 2020
    
## Practice
    
    [Tick bite](https://www.bmj.com/content/370/bmj.m3029)
    
    Published 13 August 2020
  

 

## Practice
    
    [Anosmia and loss of smell in the era of covid-19](https://www.bmj.com/content/370/bmj.m2808)
    
    Published 21 July 2020
    
## Practice
    
    [Managing heart failure related peripheral oedema in primary care](https://www.bmj.com/content/369/bmj.m2099)
    
    Published 22 June 2020
    
## Practice
    
    [Hypospadias](https://www.bmj.com/content/369/bmj.m2070)
    
    Published 17 June 2020
    
## Practice
    
    [Assessment and management of adults with asthma during the covid-19 pandemic](https://www.bmj.com/content/369/bmj.m2092)
    
    Published 08 June 2020
    
## Practice
    
    [Covid-19: a remote assessment in primary care](https://www.bmj.com/content/368/bmj.m1182)
    
    Published 25 March 2020
    
## Practice
    
    [Bowen’s disease](https://www.bmj.com/content/368/bmj.m813)
    
    Published 20 March 2020
  

 

## Practice
    
    [Groin pain in athletes](https://www.bmj.com/content/368/bmj.m559)
    
    Published 04 March 2020
    
## Practice
    
    [Adult flatfoot](https://www.bmj.com/content/368/bmj.m295)
    
    Published 24 February 2020
    
## Practice
    
    [The maternal six week postnatal check](https://www.bmj.com/content/367/bmj.l6482)
    
    Published 02 December 2019
    
## Practice
    
    [Acute vertigo](https://www.bmj.com/content/366/bmj.l5215)
    
    Published 12 September 2019
    
## Practice
    
    [A borderline HbA1c result](https://www.bmj.com/content/365/bmj.l1361)
    
    Published 11 April 2019
    
## Practice
    
    [Iliotibial band syndrome](https://www.bmj.com/content/364/bmj.l980)
    
    Published 21 March 2019

  

 

## Practice
    
    [Health anxiety](https://www.bmj.com/content/364/bmj.l774)
    
    Published 12 March 2019
    
## Practice
    
    [Treatment-refractory hypothyroidism](https://www.bmj.com/content/364/bmj.l579)
    
    Published 25 February 2019
    
## Practice
    
    [Chronic rhinosinusitis](https://www.bmj.com/content/364/bmj.l131)
    
    Published 06 February 2019
    
## Practice
    
    [Determining the reasons for poorly controlled asthma in an adolescent](https://www.bmj.com/content/364/bmj.l75)
    
    Published 21 January 2019
    
## Practice
    
    [HIV pre-exposure prophylaxis (PrEP)](https://www.bmj.com/content/364/bmj.k4681)
    
    Published 17 January 2019
    
## Practice
    
    [HIV post-exposure prophylaxis (PEP)](https://www.bmj.com/content/363/bmj.k4928)
    
    Published 29 November 2018
  






 Sort this data into three columns; Area of practice, Article Title and Link, Published date

## Practice
    
    [New diagnosis of hyperthyroidism in primary care](https://www.bmj.com/content/362/bmj.k2880)
    
    Published 24 August 2018
    
## Practice
    
    [Altitude sickness and acetazolamide](https://www.bmj.com/content/361/bmj.k2153)
    
    Published 31 May 2018
    
## Practice
    
    [Identifying post-traumatic stress disorder in forced migrants](https://www.bmj.com/content/361/bmj.k1608)
    
    Published 10 May 2018
    
## Practice
    
    [Dyslipidaemia and cardiovascular risk](https://www.bmj.com/content/360/bmj.k835)
    
    Published 23 March 2018
    
## Practice
    
    [Reduced fetal movements](https://www.bmj.com/content/360/bmj.k570)
    
    Published 06 March 2018
    
## Practice
    
    [Managing migraine in pregnancy](https://www.bmj.com/content/360/bmj.k80)
    
    Published 25 January 2018
  

 

## Practice
    
    [Birth options after a caesarean section](https://www.bmj.com/content/360/bmj.j5737)
    
    Published 11 January 2018
    
## Practice
    
    [Aural microsuction](https://www.bmj.com/content/357/bmj.j2908)
    
    Published 29 June 2017
    
## Practice
    
    [Discussing human papilloma virus vaccination](https://www.bmj.com/content/357/bmj.j2730)
    
    Published 22 June 2017
    
## Practice
    
    [Stress at work](https://www.bmj.com/content/357/bmj.j2489)
    
    Published 15 June 2017
    
## Practice
    
    [A snoring child](https://www.bmj.com/content/357/bmj.j2124)
    
    Published 18 May 2017
    
## Practice
    
    [Contraception advice for women with epilepsy](https://www.bmj.com/content/357/bmj.j2010)
    
    Published 11 May 2017
  

 

## Practice
    
    [Ongoing vomiting in an infant](https://www.bmj.com/content/357/bmj.j1802)
    
    Published 04 May 2017
    
## Practice
    
    [A likely urinary tract infection in a pregnant woman](https://www.bmj.com/content/357/bmj.j1777)
    
    Published 27 April 2017
    
## Practice
    
    [Lower urinary tract symptoms in an older man](https://www.bmj.com/content/357/bmj.j1493)
    
    Published 18 April 2017
    
## Practice
    
    [A bleeding socket after tooth extraction](https://www.bmj.com/content/357/bmj.j1217)
    
    Published 03 April 2017
    
## Practice
    
    [Paediatric hearing loss](https://www.bmj.com/content/356/bmj.j803)
    
    Published 09 March 2017
    
## Practice
    
    [Steroid modified tinea](https://www.bmj.com/content/356/bmj.j973)
    
    Published 08 March 2017
  

 

## Practice
    
    [A suspected viral rash in pregnancy](https://www.bmj.com/content/356/bmj.j512)
    
    Published 03 March 2017
    
## Practice
    
    [The offer of an HIV screen for an asymptomatic adult](https://www.bmj.com/content/356/bmj.i6656)
    
    Published 19 January 2017
    
## Practice
    
    [New diagnosis of polycystic ovary syndrome](https://www.bmj.com/content/356/bmj.i6456)
    
    Published 12 January 2017
    
## Practice
    
    [A painful tingling hand](https://www.bmj.com/content/355/bmj.i6386)
    
    Published 01 December 2016
    
## Practice
    
    [Managing recovery from concussion](https://www.bmj.com/content/355/bmj.i5629)
    
    Published 16 November 2016
    
## Practice
    
    [Haematospermia](https://www.bmj.com/content/355/bmj.i5124)
    
    Published 10 November 2016
  





 Sort this data into three columns; Area of practice, Article Title and Link, Published date

## Practice
    
    [Anal itching](https://www.bmj.com/content/355/bmj.i4931)
    
    Published 04 November 2016
    
## Practice
    
    [Anabolic steroid use](https://www.bmj.com/content/355/bmj.i5023)
    
    Published 13 October 2016
    
## Practice
    
    [Tight foreskin](https://www.bmj.com/content/355/bmj.i4639)
    
    Published 05 October 2016
    
## Practice
    
    [Recurrent otalgia in adults](https://www.bmj.com/content/354/bmj.i3917)
    
    Published 15 September 2016
    
## Practice
    
    [Poor adherence to antihypertensive drugs](https://www.bmj.com/content/354/bmj.i3268)
    
    Published 21 July 2016
    
## Practice
    
    [Acute painful breast in a non-lactating woman](https://www.bmj.com/content/353/bmj.i2646)
    
    Published 15 June 2016
  

 

## Practice
    
    [Management of a new pregnancy in a woman with chronic hypertension](https://www.bmj.com/content/353/bmj.i1497)
    
    Published 06 June 2016
    
## Practice
    
    [Tooth avulsion](https://www.bmj.com/content/353/bmj.i1394)
    
    Published 25 April 2016
    
## Practice
    
    [Stopping antidepressants following depression](https://www.bmj.com/content/352/bmj.i220)
    
    Published 18 February 2016
    
## Practice
    
    [Diagnosing chronic obstructive pulmonary disease](https://www.bmj.com/content/351/bmj.h6171)
    
    Published 24 November 2015
    
## Practice
    
    [Double vision](https://www.bmj.com/content/351/bmj.h5385)
    
    Published 18 November 2015
    
## Practice
    
    [Pelvic pain](https://www.bmj.com/content/351/bmj.h5637)
    
    Published 12 November 2015

  

 

## Practice
    
    [Reducing the risk of diabetes](https://www.bmj.com/content/351/bmj.h4595)
    
    Published 22 September 2015
    
## Practice
    
    [Assessing the risk of diabetes](https://www.bmj.com/content/351/bmj.h4525)
    
    Published 03 September 2015
    
## Practice
    
    [Bariatric surgery](https://www.bmj.com/content/351/bmj.h3802)
    
    Published 30 July 2015
    
## Practice
    
    [Nipple discharge](https://www.bmj.com/content/351/bmj.h3123)
    
    Published 21 July 2015
    
## Practice
    
    [Gradual loss of vision in adults](https://www.bmj.com/content/350/bmj.h2093)
    
    Published 08 June 2015
    
## Practice
    
    [Foot drop](https://www.bmj.com/content/350/bmj.h1736)
    
    Published 27 April 2015
  

 

## Practice
    
    [High INR on warfarin](https://www.bmj.com/content/350/bmj.h1282)
    
    Published 09 April 2015
    
## Practice
    
    [Teenagers with back pain](https://www.bmj.com/content/350/bmj.h1275)
    
    Published 02 April 2015
    
## Practice
    
    [Pain at the base of the thumb](https://www.bmj.com/content/350/bmj.h182)
    
    Published 03 February 2015
    
## Practice
    
    [The drooling child](https://www.bmj.com/content/350/bmj.h38)
    
    Published 29 January 2015
    
## Practice
    
    [Gastro-oesophageal reflux disease in children: NICE guidance](https://www.bmj.com/content/350/bmj.g7703)
    
    Published 14 January 2015
    
## Practice
    
    [Breast lumps](https://www.bmj.com/content/349/bmj.g5275)
    
    Published 05 September 2014








 Sort this data into three columns; Area of practice, Article Title and Link, Published date

## Practice
    
    [Eyelid lumps and lesions](https://www.bmj.com/content/348/bmj.g3029)
    
    Published 19 May 2014
    
## Practice
    
    [Eustachian tube dysfunction in adults](https://www.bmj.com/content/348/bmj.g1647)
    
    Published 11 March 2014
    
## Practice
    
    [Diagnosis and management of chronic heart failure](https://www.bmj.com/content/348/bmj.g1429)
    
    Published 12 February 2014
    
## Practice
    
    [Baby with an abnormal head](https://www.bmj.com/content/348/bmj.f7609)
    
    Published 10 January 2014
    
## Practice
    
    [A feeling of a lump in the throat](https://www.bmj.com/content/348/bmj.f7195)
    
    Published 07 January 2014
    
## Practice
    
    [Tremor](https://www.bmj.com/content/347/bmj.f7200)
    
    Published 12 December 2013
  

 

## Practice
    
    [Dental pain](https://www.bmj.com/content/347/bmj.f6539)
    
    Published 05 November 2013
    
## Practice
    
    [Flashes, floaters, and a field defect](https://www.bmj.com/content/347/bmj.f6496)
    
    Published 04 November 2013
    
## Practice
    
    [An adult with a neck lump](https://www.bmj.com/content/347/bmj.f5473)
    
    Published 28 October 2013
    
## Practice
    
    [Abnormal vaginal discharge](https://www.bmj.com/content/347/bmj.f4975)
    
    Published 13 August 2013
    
## Practice
    
    [Umbilical hernia](https://www.bmj.com/content/347/bmj.f4252)
    
    Published 19 July 2013
    
## Practice
    
    [A pain in the bottom](https://www.bmj.com/content/347/bmj.f4192)
    
    Published 01 July 2013
  

 

## Practice
    
    [Phimosis in childhood](https://www.bmj.com/content/346/bmj.f3678)
    
    Published 20 June 2013
    
## Practice
    
    [Atrial fibrillation](https://www.bmj.com/content/346/bmj.f3719)
    
    Published 17 June 2013
    
## Practice
    
    [Thrombocytopenia in an adult](https://www.bmj.com/content/346/bmj.f3407)
    
    Published 10 June 2013
    
## Practice
    
    [Adult acute rhinosinusitis](https://www.bmj.com/content/346/bmj.f2687)
    
    Published 10 May 2013
    
## Practice
    
    [Hearing loss in adults](https://www.bmj.com/content/346/bmj.f2496)
    
    Published 25 April 2013
    
## Practice
    
    [Vasectomy](https://www.bmj.com/content/346/bmj.f1674)
    
    Published 02 April 2013
  







Sort this data into three columns; Area of practice, Article Title and Link, Published date 

## Practice
    
    [Assessment and management of renal colic](https://www.bmj.com/content/346/bmj.f985)
    
    Published 21 February 2013
    
## Practice
    
    [Dry eye](https://www.bmj.com/content/345/bmj.e7533)
    
    Published 15 November 2012
    
## Practice
    
    [Minor incised traumatic laceration](https://www.bmj.com/content/345/bmj.e6824)
    
    Published 23 October 2012
    
## Practice
    
    [Adult trigger finger](https://www.bmj.com/content/345/bmj.e5743)
    
    Published 12 October 2012
    
## Practice
    
    [Myalgia while taking statins](https://www.bmj.com/content/345/bmj.e5348)
    
    Published 14 August 2012
    
## Practice
    
    [Otitis externa](https://www.bmj.com/content/344/bmj.e3623)
    
    Published 30 May 2012
  

 

## Practice
    
    [Blood stained nappy](https://www.bmj.com/content/344/bmj.e3496)
    
    Published 24 May 2012
    
## Practice
    
    [Blepharitis](https://www.bmj.com/content/344/bmj.e3328)
    
    Published 23 May 2012
    
## Practice
    
    [Tick bite and early Lyme borreliosis](https://www.bmj.com/content/344/bmj.e3124)
    
    Published 14 May 2012
    
## Practice
    
    [A child with neck swelling](https://www.bmj.com/content/344/bmj.e3171)
    
    Published 08 May 2012
    
## Practice
    
    [A scaly rash on the hands](https://www.bmj.com/content/344/bmj.e2252)
    
    Published 28 March 2012
    
## Practice
    
    [Epistaxis](https://www.bmj.com/content/344/bmj.e1097)
    
    Published 23 February 2012
  

 

## Practice
    
    [Varicose veins](https://www.bmj.com/content/344/bmj.e667)
    
    Published 09 February 2012
    
## Practice
    
    [Reviewing a patient with coeliac disease](https://www.bmj.com/content/344/bmj.d8152)
    
    Published 17 January 2012
    
## Practice
    
    [Dyspepsia](https://www.bmj.com/content/343/bmj.d6234)
    
    Published 30 September 2011
    
## Practice
    
    [The Hajj](https://www.bmj.com/content/343/bmj.d5593)
    
    Published 15 September 2011
    
## Practice
    
    [Measles, mumps, and rubella vaccination in a child with suspected egg allergy](https://www.bmj.com/content/343/bmj.d4536)
    
    Published 03 August 2011
    
## Practice
    
    [Osgood-Schlatter disease](https://www.bmj.com/content/343/bmj.d4534)
    
    Published 01 August 2011
  

 

## Practice
    
    [Sexual dysfunction in cardiovascular disease](https://www.bmj.com/content/343/bmj.d4437)
    
    Published 26 July 2011
    
## Practice
    
    [The Watery Eye](https://www.bmj.com/content/343/bmj.d4029)
    
    Published 19 July 2011
    
## Practice
    
    [Otitis media with effusion (“glue ear”)](https://www.bmj.com/content/343/bmj.d3770)
    
    Published 04 July 2011
    
## Practice
    
    [Chronic chilblains](https://www.bmj.com/content/342/bmj.d2708)
    
    Published 07 June 2011
    
## Practice
    
    [Otorrhoea](https://www.bmj.com/content/342/bmj.d2299)
    
    Published 20 May 2011
    
## Practice
    
    [Gilbert’s syndrome](https://www.bmj.com/content/342/bmj.d2293)
    
    Published 20 April 2011
  

 

## Practice
    
    [Epididymo-orchitis](https://www.bmj.com/content/342/bmj.d1543)
    
    Published 13 April 2011
    
## Practice
    
    [Frequent exacerbations in chronic obstructive pulmonary disease](https://www.bmj.com/content/342/bmj.d1434)
    
    Published 04 April 2011
    
## Practice
    
    [Malaria](https://www.bmj.com/content/342/bmj.d1149)
    
    Published 15 March 2011
    
## Practice
    
    [Hypoglycaemia](https://www.bmj.com/content/342/bmj.d567)
    
    Published 16 February 2011
    
## Practice
    
    [Gout](https://www.bmj.com/content/341/bmj.c6155)
    
    Published 15 November 2010
    
## Practice
    
    [Macromastia (large breasts): request for breast reduction](https://www.bmj.com/content/341/bmj.c5408)
    
    Published 13 October 2010
  

 

## Practice
    
    [Hallux valgus](https://www.bmj.com/content/341/bmj.c5130)
    
    Published 27 September 2010
    
## Practice
    
    [Chalazion](https://www.bmj.com/content/341/bmj.c4044)
    
    Published 10 August 2010
    
## Practice
    
    [Vitamin B-12 deficiency](https://www.bmj.com/content/340/bmj.c2305)
    
    Published 01 June 2010
    
## Practice
    
    [Stridor in children](https://www.bmj.com/content/340/bmj.c2193)
    
    Published 04 May 2010
    
## Practice
    
    [“My baby keeps bringing up his feeds!”](https://www.bmj.com/content/340/bmj.c2189)
    
    Published 30 April 2010
    
## Practice
    
    [Hoarse voice](https://www.bmj.com/content/340/bmj.c522)
    
    Published 07 April 2010
  








 Sort this data into three columns; Area of practice, Article Title and Link, Published date

## Practice
    
    [Sexual health consultation for men who have sex with men](https://www.bmj.com/content/340/bmj.c958)
    
    Published 22 March 2010
    
## Practice
    
    [Acute cough in adults](https://www.bmj.com/content/340/bmj.c574)
    
    Published 12 February 2010
    
## Practice
    
    [Female stress urinary incontinence](https://www.bmj.com/content/340/bmj.b5533)
    
    Published 01 February 2010
    
## Practice
    
    [Pollen food syndrome in a teenage student](https://www.bmj.com/content/340/bmj.b3405)
    
    Published 01 February 2010
    
## Practice
    
    [Malignant melanoma](https://www.bmj.com/content/339/bmj.b3078)
    
    Published 04 September 2009
    
## Practice
    
    [Tennis elbow](https://www.bmj.com/content/339/bmj.b3180)
    
    Published 02 September 2009
  

 

## Practice
    
    [Hirsutism](https://www.bmj.com/content/339/bmj.b3090)
    
    Published 28 August 2009
    
## Practice
    
    [Acute anterior uveitis](https://www.bmj.com/content/339/bmj.b2986)
    
    Published 25 August 2009
    
## Practice
    
    [Exacerbation of atopic eczema in children](https://www.bmj.com/content/339/bmj.b2997)
    
    Published 25 August 2009
    
## Practice
    
    [Herpes zoster ophthalmicus](https://www.bmj.com/content/339/bmj.b2624)
    
    Published 13 August 2009
    
## Practice
    
    [Reduced sexual desire in women](https://www.bmj.com/content/339/bmj.b2371)
    
    Published 10 August 2009
    
## Practice
    
    [Aphthous ulcers](https://www.bmj.com/content/339/bmj.b2382)
    
    Published 24 July 2009
  

 

## Practice
    
    [Non-alcoholic fatty liver disease](https://www.bmj.com/content/339/bmj.b2474)
    
    Published 16 July 2009
    
## Practice
    
    [Test of time](https://www.bmj.com/content/338/bmj.b1878)
    
    Published 15 June 2009
    
## Practice
    
    [Acne vulgaris](https://www.bmj.com/content/338/bmj.a2738)
    
    Published 05 June 2009
    
## Practice
    
    [Haematuria](https://www.bmj.com/content/338/bmj.b1324)
    
    Published 17 April 2009
    
## Practice
    
    [Transient ischaemic attack](https://www.bmj.com/content/338/bmj.a2343)
    
    Published 23 March 2009
    
## Practice
    
    [Sleep disorder (insomnia)](https://www.bmj.com/content/337/bmj.a1245)
    
    Published 28 November 2008
  

 

## Practice
    
    [Genital warts](https://www.bmj.com/content/337/bmj.a1171)
    
    Published 17 October 2008
    
## Practice
    
    [Memory problems in an older person](https://www.bmj.com/content/337/bmj.a1170)
    
    Published 10 October 2008
    
## Practice
    
    [Raised blood glucose concentration](https://www.bmj.com/content/337/bmj.a1073)
    
    Published 25 September 2008
    
## Practice
    
    [New patient asking for a benzodiazepine prescription](https://www.bmj.com/content/337/bmj.a658)
    
    Published 28 August 2008
    
## Practice
    
    [Chronic diarrhoea in a teenager](https://www.bmj.com/content/337/bmj.39490.625197.BE)
    
    Published 14 July 2008
    
## Practice
    
    [Suspected premature menopause](https://www.bmj.com/content/336/7648/833)
    
    Published 10 April 2008
  

 

## Practice
    
    [Management of recurrent gout](https://www.bmj.com/content/336/7639/329)
    
    Published 07 February 2008
    
## Practice
    
    [Otalgia](https://www.bmj.com/content/336/7638/276)
    
    Published 31 January 2008
    
## Practice
    
    [Smoking cessation](https://www.bmj.com/content/336/7637/217)
    
    Published 24 January 2008
    
## Practice
    
    [Occupational dermatitis in a hairdresser](https://www.bmj.com/content/335/7616/399)
    
    Published 23 August 2007
    
## Practice
    
    [Chronic knee pain](https://www.bmj.com/content/335/7614/303)
    
    Published 09 August 2007
    
## Practice
    
    [Chronic kidney disease](https://www.bmj.com/content/334/7606/1273)
    
    Published 14 June 2007
  

 

## Practice
    
    [Tiredness](https://www.bmj.com/content/334/7605/1221)
    
    Published 07 June 2007
    
## Practice
    
    [10-minute consultation: sinusitis](https://www.bmj.com/content/334/7604/1165)
    
    Published 31 May 2007
    
## Practice
    
    [Chronic obstructive pulmonary disease](https://www.bmj.com/content/334/7597/798)
    
    Published 12 April 2007
    
## Practice
    
    [Intermittent claudication](https://www.bmj.com/content/334/7596/746)
    
    Published 05 April 2007
    
## Practice
    
    [Dry mouth](https://www.bmj.com/content/334/7592/534)
    
    Published 08 March 2007
    
## Practice
    
    [Olfactory loss](https://www.bmj.com/content/334/7590/423)
    
    Published 22 February 2007
  








Sort this data into three columns; Area of practice, Article Title and Link, Published date
## Practice
    
    [Collapse with loss of awareness](https://www.bmj.com/content/334/7585/153)
    
    Published 18 January 2007
    
## Practice
    
    [Problem drug use](https://www.bmj.com/content/333/7569/639)
    
    Published 21 September 2006
    
## Practice
    
    [Preventing development of allergic disorders in children](https://www.bmj.com/content/333/7566/485)
    
    Published 31 August 2006
    
## Practice
    
    [Erectile dysfunction](https://www.bmj.com/content/332/7541/593)
    
    Published 09 March 2006
    
## Primary care
    
    [Snoring](https://www.bmj.com/content/331/7524/1063)
    
    Published 03 November 2005
    
## Primary care
    
    [Cancer prevention](https://www.bmj.com/content/331/7517/618)
    
    Published 15 September 2005
  

 

## Primary care
    
    [Childhood eczema](https://www.bmj.com/content/331/7515/497)
    
    Published 01 September 2005
    
## Primary care
    
    [Red eye](https://www.bmj.com/content/331/7514/438)
    
    Published 18 August 2005
    
## Primary care
    
    [Anaphylaxis](https://www.bmj.com/content/331/7512/330.1)
    
    Published 04 August 2005
    
## Primary care
    
    [Vertigo](https://www.bmj.com/content/330/7490/523)
    
    Published 03 March 2005
    
## Primary care
    
    [Tinnitus](https://www.bmj.com/content/330/7485/237)
    
    Published 27 January 2005
    
## Primary care
    
    [Family history of breast cancer](https://www.bmj.com/content/330/7481/26)
    
    Published 30 December 2004
  

 

## Primary care
    
    [Newly diagnosed hypothyroidism](https://www.bmj.com/content/329/7477/1271)
    
    Published 25 November 2004
    
## Primary care
    
    [Using the NO TEARS tool for medication review](https://www.bmj.com/content/329/7463/434)
    
    Published 19 August 2004
    
## Primary care
    
    [Female dyspareunia](https://www.bmj.com/content/328/7452/1357)
    
    Published 03 June 2004
    
## Primary care
    
    [Management of diastolic heart failure in older adults](https://www.bmj.com/content/328/7448/1114)
    
    Published 06 May 2004
    
## Primary care
    
    [Acute cough in children](https://www.bmj.com/content/328/7447/1062)
    
    Published 29 April 2004
    
## Primary care
    
    [Persistent crying in babies](https://www.bmj.com/content/328/7435/330)
    
    Published 05 February 2004
  

 

## Primary care
    
    [Recurrent urinary tract infection in women](https://www.bmj.com/content/327/7425/1204)
    
    Published 20 November 2003
    
## Primary care
    
    [Cervical_Chlamydia trachomatis_infection](https://www.bmj.com/content/327/7420/910)
    
    Published 16 October 2003
    
## Primary care
    
    [Acute low back pain](https://www.bmj.com/content/327/7414/541)
    
    Published 04 September 2003
    
## Primary care
    
    [High result in prostate specific antigen test](https://www.bmj.com/content/327/7411/379)
    
    Published 14 August 2003
    
## Primary care
    
    [Newly diagnosed type 2 diabetes mellitus](https://www.bmj.com/content/326/7403/1371)
    
    Published 19 June 2003
    
## Primary care
    
    [Adverse drug event](https://www.bmj.com/content/326/7397/1018)
    
    Published 10 May 2003
  








 
Sort this data into three columns; Area of practice, Article Title and Link, Published date
## Primary care
    
    [Polyarthralgia](https://www.bmj.com/content/326/7394/859)
    
    Published 19 April 2003
    
## Primary care
    
    [Chronic low back pain](https://www.bmj.com/content/326/7388/535)
    
    Published 08 March 2003
    
## Primary care
    
    [Food allergy](https://www.bmj.com/content/325/7376/1337)
    
    Published 07 December 2002
    
## Primary care
    
    [Gastro-oesophageal reflux disease](https://www.bmj.com/content/325/7370/945)
    
    Published 26 October 2002
    
## Correction
    
    [10-minute consultation: Paraesthesia](https://www.bmj.com/content/325/7359/304.4)
    
    Published 10 August 2002
    
## Primary care
    
    [Removal of ear wax](https://www.bmj.com/content/325/7354/27)
    
    Published 06 July 2002
  

 

## Primary care
    
    [Paraesthesia](https://www.bmj.com/content/324/7352/1501)
    
    Published 22 June 2002
    
## Primary care
    
    [Newly diagnosed hypertension](https://www.bmj.com/content/324/7350/1375)
    
    Published 08 June 2002
    
## Primary care
    
    [Genital herpes](https://www.bmj.com/content/324/7345/1076)
    
    Published 04 May 2002
    
## Primary care
    
    [Rhinitis](https://www.bmj.com/content/324/7334/403)
    
    Published 16 February 2002
    
## Primary care
    
    [First episode psychosis](https://www.bmj.com/content/323/7326/1408)
    
    Published 15 December 2001
    
## Primary care
    
    [MMR immunisation](https://www.bmj.com/content/323/7303/32)
    
    Published 07 July 2001
  

 

## Primary care
    
    [Prostatic symptoms](https://www.bmj.com/content/322/7300/1468.1)
    
    Published 16 June 2001
    
## Primary care
    
    [Dyspepsia](https://www.bmj.com/content/322/7289/776)
    
    Published 31 March 2001
    
## Primary care
    
    [Binge eating](https://www.bmj.com/content/322/7282/343)
    
    Published 10 February 2001
    
## General practice
    
    [Menorrhagia](https://www.bmj.com/content/321/7266/935)
    
    Published 14 October 2000
    
"""
# Parsing patterns  (with flexibility)
practice_pattern = r"## Practice (.+)"
link_pattern = r"\[([^\]]+)\]\((https?://[^\)]+)\)"  
date_pattern = r"Published (\d{1,2} \w+ \d{4})"  # More flexible month capture

# Extracted data
entries = []

# Iterate through the data in chunks (more robust splitting)
for chunk in re.split(r"## Practice|\n-", data): 
    chunk = chunk.strip()
    if chunk:  
        # Extracting data using a more forgiving approach
        practice_match = re.search(practice_pattern, chunk)
        links = re.findall(link_pattern, chunk)  # Find all links
        dates = re.findall(date_pattern, chunk)  # Find all dates

        if practice_match:
            for link, date in zip(links, dates):  # Pair links and dates
                entries.append({
                    "Area of Practice": practice_match.group(1).strip(),
                    "Article Title": link[0],
                    "Article Link": link[1],
                    "Published Date": date
                })

# ... (rest of the code for writing to the file remains the same)

# Write results to a file
with open("article_data.txt", "w", encoding="utf-8") as outfile:  # Open file in write mode with UTF-8 encoding
    # Header row
    outfile.write(f"| {'Area of Practice':<40} | {'Article Title':<60} | {'Article Link'} | {'Published Date'} |\n")
    outfile.write(f"|:{'-' * 40}-|:{'-' * 60}-|:{'-' * 15}-|:{'-' * 15}-|\n")  # Separator line

    # Data rows
    for entry in entries:
        outfile.write(f"| {entry['Area of Practice']:<40} | {entry['Article Title']:<60} | {entry['Article Link']} | {entry['Published Date']} |\n")

import tkinter as tk
from tkinter import ANCHOR, font
from tkinter import ttk
from turtle import color, left
from tabulate import tabulate
import sys

def submit():
    name = name_entry.get()
    roll_number = roll_entry.get()

    if not name or not roll_number or any(char.isdigit() for char in name):
        submit_button.configure(style="Error.TButton")
    else:
        submit_button.configure(style="TButton")
        win_152.destroy()

        print("Name of the user:",name)
        print("Roll number of the user:",roll_number)


        def but_clicked(but_num):
            if but_num == 1:

                intro1 = """→ Organic compounds are vital for sustaining life on Earth and they include complex molecules like
            genetic information-bearing Deoxyribo-Nueclic Acid (DNA) and proteins that constitute essential compounds of
            our blood, muscles, and skin.\n\n"""
                intro1 += """→ Science of Organic Chemistry is about 200 years old. Around 1780, chemists began to distinguish
            between organic compounds obtained from plants and animals and inorganic compounds prepared from mineral sources.\n\n"""
                intro1 += """→ It is a vast field of chemistry that is centered around the element carbon and its interactions
            with other elements, including hydrogen, oxygen, nitrogen, sulfur, and many others."""
                win_1 = tk.Toplevel()
                win_1.title("Introduction")
                custom_font = font.Font(size=12)
                info_label = tk.Label(win_1, text=intro1, font=custom_font, justify="left")
                info_label.pack()
                destroy = ttk.Button(win_1, text="Exit", command=win_1.destroy)
                destroy.pack(anchor="w")


            elif but_num == 2:

                intro2 = "→ Organic compounds are compounds that contain carbon atoms.\n\n"
                intro2 += "→ They can be found in living organisms, such as carbohydrates, proteins, lipids, and nucleic acids.\n\n"
                intro2 += "→ Organic compounds also include synthetic materials like plastics, dyes, and pharmaceuticals.\n\n"

                win_2 = tk.Toplevel()
                win_2.title("Organic compounds")
                custom_font = font.Font(size=12)
                info_1 = tk.Label(win_2, text=intro2, font=custom_font, justify="left")
                info_1.pack()
                destroy_2 = ttk.Button(win_2, text="Exit", command=win_2.destroy)
                destroy_2.pack(anchor="w")
                
                


            elif but_num == 3:

                intro3 = """→A Functional Group may be defined as an atom or group of atoms joined in a specfic manner which is responsible for the 
                characteristic chemical properties of the Organic Compounds.\n\n"""
                intro3 += ("""Ex: →Hydroxyl Group-(-OH)\n
                →Aldehyde Group-(CHO)\n
                →Carboxylic Acid Group-(-COOH)\n""")

                win_3 = tk.Toplevel()
                win_3.title("Functional groups")
                custom_font = font.Font(size=12)
                info_2 = tk.Label(win_3, text=intro3, font=custom_font, justify="left")
                info_2.pack()

                def class_fg():
                    intro4 = """1.Hydrocarbon Functional Groups:

                »Alkyl Group (-R): Consists of a chain of carbon atoms bonded exclusively to hydrogen atoms.
                »Alkenes (-C=C-): Contain a carbon-carbon double bond.
                »Alkynes (-C≡C-): Contain a carbon-carbon triple bond.
                »Aromatic Ring (e.g., benzene ring): Consists of a conjugated ring of carbon atoms with alternating single and double bonds.\n\n"""

                    intro4 += """2.Oxygen-Containing Functional Groups:

                »Alcohol (-OH): Contains a hydroxyl group bonded to a carbon atom.
                »Ether (-O-): Comprises an oxygen atom bonded to two carbon groups.
                »Aldehyde (-CHO): Contains a carbonyl group at the end of a carbon chain.
                »Ketone (-C(=O)-): Contains a carbonyl group in the middle of a carbon chain.
                »Carboxylic Acid (-COOH): Consists of a carbonyl group and a hydroxyl group bonded to the same carbon atom.
                »Ester (-COO-): Contains a carbonyl group bonded to an oxygen atom and another carbon atom.
                »Amide (-CONH-): Contains a carbonyl group bonded to a nitrogen atom and a carbon atom.
                »Peroxide (-O-O-): Contains an oxygen-oxygen single bond.\n\n"""

                    intro4 += """3.Nitrogen-Containing Functional Groups:

                »Amine (-NH2): Contains a nitrogen atom bonded to one or more carbon atoms.
                »Amide (-CONH-): Contains a carbonyl group bonded to a nitrogen atom and a carbon atom.\n\n"""

                    intro4 += """4.Halogen-Containing Functional Groups:

                »Alkyl Halide (Ex: -Cl, -Br, -I): Contains a halogen atom (chlorine, bromine, or iodine) bonded to a carbon atom.\n\n"""

                    intro4 += """5.Sulfur-Containing Functional Groups:

                »Thiol (-SH): Contains a sulfur atom bonded to a carbon atom.
                »Sulfide (-S-): Contains a sulfur atom bonded to two carbon groups.
                »Sulfoxide (-S=O-): Contains a sulfur atom bonded to a carbon atom and an oxygen atom.
                »Sulfone (-S=O₂-): Contains a sulfur atom bonded to two carbon groups and two oxygen atoms.\n\n"""

                    intro4 += "These classifications provide a framework for identifying and categorizing functional groups based on their composition and properties\n\n"

                    win_4 = tk.Toplevel()
                    win_4.title("Classifications of functional groups")
                    custom_font = font.Font(size=12)
                    info_4 = tk.Label(win_4, text=intro4, font=custom_font, justify="left")
                    info_4.pack()
                    destroy_4 = ttk.Button(win_4, text="Exit", command=win_4.destroy)
                    destroy_4.pack(anchor="w")

                def role_fg():
                    intro5 = """Functional groups play a key role in Organic Chemistry  due to their significant influence on the chemical properties and reactivity of organic compounds.\n\n"""
                    intro5 += """1.Chemical Reactivity: Functional groups determine how a molecule will react with other substances.
                                The presence of a functional group can make a molecule more or less reactive, as it provides specific sites for chemical reactions to occur. 
                                Ex: the presence of a carbonyl group in aldehydes and ketones allows them to undergo nucleophilic addition reactions.\n"""
                    intro5 += """2.Intermolecular Interactions: Functional groups influence the intermolecular forces between molecules, affecting properties such as 
                                boiling points, melting points, and solubility. For instance, the presence of hydrogen bonding in molecules containing hydroxyl groups (alcohols) 
                                leads to higher boiling points and increased solubility in water.\n\n"""
                    intro5 += """3.Acidity and Basicity: Functional groups can determine the acidity or basicity of organic compounds. For example, carboxylic acids (-COOH) 
                                are acidic due to the presence of the carboxyl group, while amines (-NH2) can act as bases. The presence of functional groups with acidic or basic properties 
                                greatly affects the reactivity and behavior of the compounds.\n\n"""
                    intro5 += """4.Structural Identification: Functional groups serve as structural features that help identify and classify organic compounds. By analyzing the 
                                presence of specific functional groups, chemists can identify and categorize organic molecules, enabling the prediction of their behavior and properties.\n\n"""
                    intro5 += """5.Synthetic Strategies: Functional groups play a crucial role in synthetic organic chemistry. Chemists use functional groups as points of manipulation 
                                to introduce or modify specific properties in organic molecules. Functional group transformations, such as functional group interconversions, allow the synthesis 
                                of complex organic compounds.\n\n"""
                    intro5 += "Etc....."

                    win_5 = tk.Toplevel()
                    win_5.title("Role of functional groups in organic chemistrty")
                    custom_font = font.Font(size=12)
                    info_5 = tk.Label(win_5, text=intro5, font=custom_font, justify="left")
                    info_5.pack()
                    destroy_5 = ttk.Button(win_5, text="Exit", command=win_5.destroy)
                    destroy_5.pack(anchor="w")

                but_classfg = ttk.Button(win_3, text="Classifications of functional groups", command=class_fg,width=60)
                but_rolefg = ttk.Button(win_3, text="Role of functional groups in organic chemistry.", command=role_fg, width=60)
                but_classfg.pack(anchor="w")
                but_rolefg.pack(anchor="w")
                destroy_3 = ttk.Button(win_3, command=win_3.destroy, text="Exit", width=60)
                destroy_3.pack(anchor="w")


            elif but_num == 4:

                intro6 = """→Hydrocarbons are organic compounds composed of hydrogen and carbon atoms. They are the fundamental building blocks 
                of many important substances,including fossil fuels like natural gas, petroleum (oil), and coal. Hydrocarbons are also present 
                in various other forms, such as methane (CH₄), ethane (C₂H₆), 
                propane (C₃H₈), butane (C₄H₁₀), and so on.\n\n"""

                win_6 = tk.Toplevel()
                win_6.title("Hydrocarbons")
                custom_font = font.Font(size=12)
                info_6 = tk.Label(win_6, text=intro6, font=custom_font, justify="left")
                info_6.pack()

                def al_hc():
                    intro7 = """→An aliphatic compound or aliphatic hydrocarbon contains hydrogen and carbon atoms linked together in straight chains. 
            Sometimes, the chains can also occur in branched form or non-aromatic structures. Keep in mind that aliphatic compounds are organic. 
            Apart from the hydrogen, different elements like oxygen, nitrogen, chlorine, and sulfur may get joined with the carbon atoms in the chain.\n\n"""
                    intro7 += "Properties of Aliphatic hydrocarbons:\n\n"
                    intro7 += """»A great majority of aliphatic compounds are flammable. They often get used as fuel sources like methane, propane, ethylene, 
            acetylene, and so on.\n\n """
                    intro7 += """»Aliphatic compounds may be cyclic or acyclic. They can have close chains or rings of carbon atoms in their molecules.\n\n"""
                    intro7 += """»When two alkanes have equal molecular mass, the more highly branched alkane has a lower boiling point. The melting points 
            for aliphatic compounds increase with size, but in a less typical manner.\n\n"""
                    intro7 += """»Since the hydrocarbons are nonpolar, they are insoluble in water and other polar solvents. However, they get dissolved in 
            non-polar solvents like benzene and diethyl ether. Also, note that hydrocarbons are less dense than water, and they can stay afloat on water surfaces.\n\n"""
                    intro7 += "→Here are some examples of Aliphatic Hydrocarbons and the no. of carbons they contatain:\n"
                    intro7 += """
                »Methane-1
                »Ethane,Ethene,Ethyne-2
                »Propane,Propene,Propyne,Cyclo-propane-3
                »Methyl-propane,Butane,Cyclo-butane-4
                »Pentane,Cyclo-pentene,Di-methyl-propane-5
                »Hexane,Cyclo-Hexane,Cyclo-Hexene-6
                Etc......"""

                    win_7 = tk.Toplevel()
                    win_7.title("Aliphatic-Hydrocarbons")
                    custom_font = font.Font(size=12)
                    info_7 = tk.Label(win_7, text=intro7, font=custom_font, justify="left")
                    info_7.pack()
                    destroy_7 = ttk.Button(win_7, text="Exit", command=win_7.destroy, width=40)
                    destroy_7.pack(anchor="w")

                def am_hc():
                    intro8 = """→Aromatic hydrocarbons are a class of organic compounds that contain a specific ring-like structure called an aromatic ring or benzene ring. 
                The most well-known aromatic hydrocarbon is benzene (C₆H₆).\n\n"""
                    intro8 += "Properties of Aromatic hydrocarbons:\n"
                    intro8 += """»Aromatic hydrocarbons exhibit a property called aromaticity. Aromatic compounds are exceptionally stable and have a lower energy state 
                compared to non-aromatic compounds.\n\n """
                    intro8 += "» The carbon atoms within a ring lie in the same plane, allowing for efficient overlap of the p-orbitals and the delocalization of electrons.\n\n"
                    intro8 += "»Aromatic compounds can be represented using resonance structures, which are different ways of distributing the π electrons within the ring.\n\n"
                    intro8 += """»Aromatic hydrocarbons typically have low solubility in water but are soluble in organic solvents. They are often volatile compounds with 
                relatively low boiling points.\n\n"""

                    win_8 = tk.Toplevel()
                    win_8.title("Aromatic-Hydrocarbons")
                    custom_font = font.Font(size=12)
                    info_8 = tk.Label(win_8, text=intro8, font=custom_font, justify="left")
                    info_8.pack()
                    destroy_8 = ttk.Button(win_8, text="Exit", command=win_8.destroy,width=40)
                    destroy_8.pack(anchor="w")

                def diff_al_am():
                    intro9 = [
                        ["Structure", "Straight or branched chains", "Benzene ring or fused rings"],
                        ["Bonding", "Single bonds", "Delocalized pi bonds"],
                        ["Hybridization", "sp3 hybridization", "sp2 hybridization"],
                        ["Reactivity", "Less reactive", "More reactive"],
                        ["Boiling Point", "Lower boiling point", "Higher boiling point"],
                        ["Odor", "Typically odorless", "Distinctive aromatic odor"],
                        ["Examples", "Ethane, Propane", "Benzene, Toluene"]
                    ]

                    win_9 = tk.Tk()
                    win_9.title("Differences between Aliphatic and Aromatic Hydrocarbons")
                    table_frame_9 = tk.Frame(win_9)
                    table_frame_9.pack()
                    tab_9 = ttk.Treeview(table_frame_9, columns=("Column1", "Column2"))
                    tab_9.heading("#0", text="Property")
                    tab_9.heading("Column1", text="Aliphatic Hydrocarbons")
                    tab_9.heading("Column2", text="Aromatic Hydrocarbons")
                    
                    
                    tab_9.pack()

                    for item in intro9:
                        tab_9.insert("", tk.END, text=item[0], values=(item[1], item[2]))

                    destroy_50 = ttk.Button(win_9, text="Exit", command=win_9.destroy,width=40,)
                    destroy_50.pack(anchor="w")

                    win_9.mainloop()

                but_alhc = ttk.Button(win_6, text="Aliphatic Hydrocarbons", command=al_hc, width=70)
                but_amhc = ttk.Button(win_6, text="Aromatic Hydrocarbons", command=am_hc, width=70)
                but_diff_alam = ttk.Button(win_6, text="Differences between Aliphatic and Aromatic Hydrocarbons",command=diff_al_am, width=70)
                destroy_6 = ttk.Button(win_6, text="Exit", command=win_6.destroy, width=70)
                but_alhc.pack(anchor="w")
                but_amhc.pack(anchor="w")
                but_diff_alam.pack(anchor="w")
                destroy_6.pack(anchor="w")


            elif but_num == 5:

                intro10 = """→In organic chemistry, nomenclature refers to the set of rules and conventions used to assign names to organic compounds. 
            It provides a systematic and standardized way of naming organic molecules, allowing chemists to communicate effectively and unambiguously about different compounds.\n\n"""
                intro10 += "→The International Union of Pure and Applied Chemistry (IUPAC) has played a central role in proposing and standardizing organic nomenclature.\n\n"
                intro10 += "→It can be said that Nomenclature is \"System of naming compounds\".\n\n"
                intro10 += "→The format of the IUPAC Name of the Compound can be written as: Word Root + Prefix + Suffix.\n\n"

                win_10 = tk.Toplevel()
                win_10.title("Nomenclature")
                custom_font = font.Font(size=12)
                info_10 = tk.Label(win_10, text=intro10, font=custom_font, justify="left")
                info_10.pack()

                def rls_nmncl():
                    intro11 = """→There are some rules to be followed while naming the various no.of compounds in orgainc chemistry.")
                    They are:\n"""
                    intro11 += """»The Longest Chain Rule: The parent hydrocarbon must be identified and subsequently named. The parent chain belonging to the compound in question is generally 
                    the longest chain of carbon atoms, be it in the form of a straight chain or a chain of any other shape.\n\n"""
                    intro11 += """»The Lowest Set of Locants: The carbon atoms belonging to the parent hydrocarbon chain must be numbered using natural numbers and beginning from the end in 
                    which the lowest number is assigned to the carbon atom which carries the substituents.\n\n"""
                    intro11 += """»Multiple instances of the same substituent: Prefixes which indicate the total number of the same substituent in the given organic compounds are given, 
                    such as di, tri, etc.\n\n"""
                    intro11 += """»Naming of different substituents: Inu the organic compounds containing multiple substituents, the corresponding substituents are arranged in 
                    alphabetical order of names in the IUPAC nomenclature of organic compounds in question.\n\n"""
                    intro11 += """»The naming of different substituents present at the same positions: In the scenario wherein two differing substituent groups are present at the same 
                    position of the organic compound, the substituents are named in ascending alphabetical order.\n\n"""
                    intro11 += """»Naming Complex Substituents: Complex substituents of organic compounds having branched structures must be named as substituted alkyl groups whereas 
                    the carbon which is attached to the substituent group is numbered as one. These branched and complex substituents must be written in brackets in the IUPAC 
                    nomenclature of the corresponding compounds.\n\n"""

                    win_11 = tk.Toplevel()
                    win_11.title("Rules of Nomenclature")
                    custom_font = font.Font(size=12)
                    info_11 = tk.Label(win_11, text=intro11, font=custom_font, justify="left")
                    info_11.pack()
                    destroy_11 = ttk.Button(win_11, text="Exit", command=win_11.destroy,width=40)
                    destroy_11.pack(anchor="w")

                def db_nmncl():
                    intro12 = """→Several trivial names can exist for one specific compound. An example of this can be observed in the alternate names of Phenol, for which names 
            such as hydroxybenzene and carbolic acid also exist.\n\n"""
                    intro12 += """→The Trivial nomenclature system is limited to only a few compounds in each specific group. An example of this is: the first two members 
            belonging to the carboxylic acid group have the trivial names formic acid and acetic acid. However, no trivial names exist for carboxylic acids with 
            a greater number of atoms.\n\n"""
                    intro12 += """→There exist no particular set of guidelines for the nomenclature of complex compounds in the trivial system.\n\n"""

                    win_12 = tk.Toplevel()
                    win_12.title("Drawbacks of Nomenclature")
                    custom_font = font.Font(size=12)
                    info_12 = tk.Label(win_12, text=intro12, font=custom_font, justify="left")
                    info_12.pack()
                    destroy_12 = ttk.Button(win_12, text="Exit", command=win_12.destroy, width=40)
                    destroy_12.pack(anchor="w")

                def cnvn():
                    intro13 = "In organic chemistry, a specific set of rules and conventions are followed for naming organic compounds.\n\n"
                    intro13 += "The nomenclature system used most widely is known as the International Union of Pure and Applied Chemistry (IUPAC) nomenclature.\n\n"
                    intro13 += "The IUPAC system provides a standardized and systematic approach for naming organic molecules.\n\n"
                    intro13 += "It follows the \"Prefix→Root Word→Suffux\" method"

                    win_13 = tk.Toplevel()
                    win_13.title("Convention in Nomenclature.")
                    custom_font = font.Font(size=12)
                    info_13 = tk.Label(win_13, text=intro13, font=custom_font, justify="left")
                    info_13.pack()

                    def prfx_cnvn():
                        intro14 = """→The substituents in the molecule are shown as the prefix.Prefix again has several parts known as primary prefix secondary prefix, 
                    numerical prefix and number prefix.\n\n"""
                        intro14 += "→Primary prefix: It is only applicable to cyclic compounds(Cyclo). If the compound is not cyclic, then this part is absent.\n\n"
                        intro14 += """→Secondary prefix : This tells about the second grade functional groups known as substituents. For example halogens, alkyl groups(R),
                    alkoxy groups(-OR) etc. which are written as halo, alkyl, alkoxy.\n\n"""
                        intro14 += """→Numerical prefix : When the same substituent, multiple bond or functional group is repeated twice, 
                    thrice etc., are denoted by di, tri, tetra... respectively.\n\n"""
                        intro14 += """→Number prefix : This tells about to which carbon atoms of the compound the substituent(s), multiple bond(s) or functional 
                    group(s)are attached.\n\n"""

                        intro15 = [
                            ["Secondary Prefix: Halides"],
                            ["Fluoro"],
                            ["Chloro"],
                            ["Bromo"],
                            ["Iodo"],
                        ]
                        intro16 = [
                            ["Secondary Prefix: R-Alkyl"],
                            ["CH₃-Methyl"],
                            ["C₂H₅-Ethyl"],
                            ["C₃H₇-Propyl"],
                        ]
                        intro17 = [
                            ["Secondary Prefix: Secondary Functional Groups"],
                            ["NO₂-Nitro"],
                            ["NO-Nitraso"],
                            ["OR-Alkoxy"],
                            ["OH-Hydroxy"],
                            ["NH₂-Amino"],
                            ["CHO-Formyl"],
                            ["C=O-Oxo"],
                            ["COOH-Carboxy"],
                        ]

                        win_14 = tk.Tk()
                        win_14.title("Prefixes-Convention")

                        intro_label = tk.Label(win_14, text=intro14, justify=tk.LEFT)
                        intro_label.pack(anchor="w")

                        table_frame = tk.Frame(win_14)
                        table_frame.pack()

                        table1 = ttk.Treeview(table_frame, columns=())

                        table1.pack(side=tk.LEFT)

                        for item in intro15:
                            table1.insert("", tk.END, text=item[0])

                        table2 = ttk.Treeview(table_frame, columns=())
                        table2.pack(side=tk.LEFT)

                        for item in intro16:
                            table2.insert("", tk.END, text=item[0])

                        table3 = ttk.Treeview(table_frame, columns=())

                        table3.pack(side=tk.LEFT)

                        for item in intro17:
                            table3.insert("", tk.END, text=item[0])

                        destroy_14 = ttk.Button(win_14, text="Exit", command=win_14.destroy,
                                               width=40)
                        destroy_14.pack(anchor="w")

                        win_14.mainloop()

                    def rw_cnvn():

                        intro18 = "Word Root describes the number of carbon atoms present in the molecule or the principle chain."

                        intro19 = [
                            ["No. of Carbon atoms", "Root-Word"],
                            ["C₁-1", "Meth"],
                            ["C₂-2", "Eth"],
                            ["C₃-3", "Prop"],
                            ["C₄-4", "But"],
                            ["C₅-5", "Pent"],
                            ["C₆-6", "Hex"],
                            ["C₇-7", "Hept"],
                            ["C₈-8", "Oct"],
                            ["C₉-9", "Non"],
                            ["C₁₀-10", "Dec"],
                        ]

                        win_15 = tk.Tk()
                        win_15.title("Root Words-Convention")

                        intro_label2 = tk.Label(win_15, text=intro18, justify=tk.LEFT)
                        intro_label2.pack()

                        tab_15 = ttk.Treeview(win_15, columns=())

                        
                        tab_15.pack()

                        for item in intro19:
                            tab_15.insert("", tk.END, text=item[0], values=(item[1]))

                        destroy_15 = ttk.Button(win_15, text="Exit", command=win_15.destroy,width=40)
                        destroy_15.pack(anchor="w")

                        win_15.mainloop()

                    def sfx_cnvn():
                        intro20 = """→The suffix in IUPAC nomenclature is usually a functional group belonging 
                    to the molecule which follows the root of the name.\n\n"""
                        intro20 += "→It can be further divided into the following types:\n2. Primary Suffix\n2. Secondary Suffix\n\n"
                        intro20 += """»Primary Suffix: This tells about the \"saturation of the compound\".
                    »For saturated (C-C) single bonded compounds, it is ‘ane’.
                    »For unsaturated (C=C) double bonded compounds, it is ‘ene’.
                    »For unsaturated triple bonded (C≡C) compounds, it is ‘yne’\n\n"""
                        intro20 += """»Secondary suffix: This tells about the functional groups with the particular term. While 
                    writing the names of the derivatives of hydrocarbons, the last letter ‘e’ of ane, ene, yne is 
                    dropped if the suffix starts with a vowel. ‘e’ should be maintained if the suffix including numerical prefix 
                    starts with a consonant.\n\n"""
                        intro20 += """    »For hydrocarbons, it is ‘–e’
                    »For alcohols, it is ‘–ol’
                    »For aldehydes, it is ‘–al’
                    »For ketones, it is ‘–one’
                    »For carboxylic acid, it is ‘–oic acid’, etc....\n\n"""

                        intro21 = [

                            ["Saturated single bonded compounds (C-C)", "-ane"],
                            ["Unsaturated double bonded compounds (C=C)", "-ene"],
                            ["Unsaturated triple bonded compounds (C≡C)", "-yne"]
                        ]

                        intro22 = [

                            ["Hydrocarbons-CH", "-e"],
                            ["Alcohols-OH", "-ol"],
                            ["Aldehydes-CHO", "-al"],
                            ["Ketones-C=O", "-one"],
                            ["Carboxylic Acids-COOH", "-oic-acid"],
                            ["Amines-NH₂", "-amine"],
                            ["Ester-COOR", "-oate"]
                        ]

                        win_16 = tk.Tk()
                        win_16.title("Suffix-Convention")

                        intro_lab15 = tk.Label(win_16, text=intro20, justify=tk.LEFT)
                        intro_lab15.pack(anchor="w")

                        table_frame = tk.Frame(win_16)
                        table_frame.pack()

                        tab20 = ttk.Treeview(table_frame, columns=("Column1"))
                        tab20.heading("#0", text="Compound Type-Suffix")



                        tab20.pack(side=tk.LEFT)
                        for item in intro21:
                            tab20.insert("", tk.END, text=item[0], values=(item[1]))

                        tab21 = ttk.Treeview(table_frame, columns=("Column1"))
                        tab21.heading("#0", text="Compound type-Suffix")


                     
                        tab21.pack(side=tk.LEFT)

                        for item in intro22:    # R. Akhilendra
                            tab21.insert("", tk.END, text=item[0], values=(item[1]))

                        destroy_20 = ttk.Button(win_16, text="Exit", command=win_16.destroy, width=40)
                        destroy_20.pack(anchor="w")

                        win_16.mainloop()

                    but_prfx_nmncl = ttk.Button(win_13, text="Prefix", command=prfx_cnvn,width=40)
                    but_prfx_nmncl.pack(anchor="w")

                    but_rw_nmncl = ttk.Button(win_13, text="Root Word", command=rw_cnvn,width=40)
                    but_rw_nmncl.pack(anchor="w")

                    but_sfx_nmncl = ttk.Button(win_13, text="Suffix", command=sfx_cnvn, width=40)
                    but_sfx_nmncl.pack(anchor="w")

                    destroy_21 = ttk.Button(win_13, text="Exit", command=win_13.destroy,width=40)
                    destroy_21.pack(anchor="w")

                but_rls_nmncl = ttk.Button(win_10, text="Rules of Nomenclature", command=rls_nmncl,width=40)
                but_rls_nmncl.pack(anchor="w")
                but_db_nmncl = ttk.Button(win_10, text="Drawbacks of Nomenclature", command=db_nmncl,width=40) 
                but_db_nmncl.pack(anchor="w")
                but_cnvn_nmncl = ttk.Button(win_10, text="Convention in Nomenclature", command=cnvn,width=40)
                but_cnvn_nmncl.pack(anchor="w")
                destroy_10 = ttk.Button(win_10, text="Exit", command=win_10.destroy,width=40)
                destroy_10.pack(anchor="w")
                

            elif but_num == 6:
                data8 = [
                    ["1", "CH₃–CH₂–CH₂–CH₃       : Butane"],
                    ["2", "CH₃–CH₂–CH=CH₂        : But-1-ene"],
                    ["3", "CH₃–CH–CH₂–CH₃        : 2-Chloro butane\n|\nCl"],
                    ["4", "CH₃–CH–CH–CH₃         : 2, 3 – dichloro butane\n|   |\nCl  Cl"],
                    ["5", "CH₃–CH=C=CH₂          : Buta 1, 2- diene"],
                    ["6", "CH₃–CH₂–CH₂–CH₂–OH    : Butan – 1 – ol"],
                    ["7", "CH₃–CH₂–CH₂–CHO       : Butanal"],
                    ["8", "CH₂–CH₂               : Cyclo butane\n|   |\nCH₂–CH₂"],
                    ["9", "Br  Br                : 1,2 – Di bromo cyclo butane\n|    |\nCH – CH\n|    |\nCH₂– CH₂"],
                    ["10", "CH₃–C–CH₂–CH₂–CH₃     : Penta n – 2 - one\n          ‖\n          O"],
                    ["11", "CH₂–CH–CHO            : 2, 3 – di chloro propanal\n|  |\nCl Cl"],
                    ["12",
                     "CH₂=C=C–CH–CH₂–CH2–CH–CH2\n|          |   |     :5 – chloro–octa–6,7–di en–1,2–di ol\nCl         OH OH"]
                ]

                win_51 = tk.Tk()
                win_51.title("Basic Examples of Organic compounds")

                info_label_51 = tk.Label(win_51, text="Here are some examples of some basic organic compounds:", anchor="w")
                info_label_51.pack(anchor="w")

                table_str_51 = tabulate(data8, headers=["No.", "Chemical Compound"], tablefmt="grid")

                table_label_51 = tk.Label(win_51, text=table_str_51, justify=tk.LEFT, font=("Courier", 10))
                table_label_51.pack()

                destroy_51 = ttk.Button(win_51, text="Exit", command=win_51.destroy, width=40)
                destroy_51.pack(anchor="w")

                win_51.mainloop()
                
            elif but_num == 7:
            
                intro_info =  "R. Akhilendra-2211CS010493\n\n"
                intro_info += "S. Geeta Velan-2211CS010526\n\n"
                intro_info1 = "S. Srivalli-2211CS010537\n\n"
                intro_info += "B. Sai Preethi-2211CS010471\n\n"
                intro_info += "P. Sahasra-2211CS010472\n"
                               
                win_info=tk.Tk()
                win_info.title("Group-4: Members")
                
                info_info = tk.Label(win_info,text=intro_info,anchor="w")
                info_info.pack(anchor="w")
                info_info1=tk.Label(win_info,text=intro_info1,anchor="w")
                info_info1.pack(anchor="w")
                
                destroy_info=ttk.Button(win_info,text="Exit",command=win_info.destroy,width=40)
                destroy_info.pack(anchor="w")
                


        window = tk.Tk()
        window.title("CHEM-ACK®")
     

        style = ttk.Style()
        style.configure("TButton",
                        foreground="black",
                        background="white",
                        width=20,
                        height=100)

        style.map("TButton",
                  foreground = [('active', '!disabled', 'blue')],
                  background = [('active', 'pink')])
        
        
        
        
        info_119="Welcome"+" "+name+"!!!"
        info_120= "roll: "+roll_number                       
        intro_info_119= tk.Label(window,text=info_119,anchor="w")
        
        intro_info_120= tk.Label(window,text=info_120,anchor="w")
        intro_info_119.pack(anchor="w")
        intro_info_120.pack(anchor="w")
        button1 = ttk.Button(window, text="Introduction", command=lambda: but_clicked(1), width=40)
        button2 = ttk.Button(window, text="Organic compounds", command=lambda: but_clicked(2), width=40)
        button3 = ttk.Button(window, text="Functional Groups", command=lambda: but_clicked(3),  width=40)
        button4 = ttk.Button(window, text="Hydrocarbons", command=lambda: but_clicked(4),  width=40)
        button5 = ttk.Button(window, text="Nomenclature", command=lambda: but_clicked(5), width=40)
        button6 = ttk.Button(window, text="Examples", command=lambda: but_clicked(6),  width=40)
        button7 = ttk.Button(window, text="Info", command=lambda: but_clicked(7),  width=40)
        button8 = ttk.Button(window, text="Exit", command=lambda: sys.exit(), width=40)

        button1.pack(anchor="n")
        button2.pack(anchor="w")
        button3.pack(anchor="w")
        button4.pack(anchor="w")
        button5.pack(anchor="w")
        button6.pack(anchor="w")
        button7.pack(anchor="w")
        button8.pack(anchor="w")
        
        window.mainloop()

def focus_roll_entry(event):
    roll_entry.focus_set()

def submit_form(event):  
    submit()


win_152 = tk.Tk()
win_152.title("Login-Page")
win_152.geometry("300x150")


frame = ttk.Frame(win_152, padding=10)
frame.pack(fill="both", expand=True)


name_label = ttk.Label(frame, text="Name:")
name_label.grid(row=0, column=0, sticky=tk.W)


name_entry = ttk.Entry(frame)
name_entry.grid(row=0, column=1, sticky=tk.W)
name_entry.bind("<Return>", focus_roll_entry)


roll_label = ttk.Label(frame, text="Roll Number:")
roll_label.grid(row=1, column=0, sticky=tk.W)


roll_entry = ttk.Entry(frame)
roll_entry.grid(row=1, column=1, sticky=tk.W)
roll_entry.bind("<Return>", submit_form)


style = ttk.Style()
style.configure("Error.TButton", foreground="red", background="red")



submit_button = ttk.Button(frame, text="Submit", command=submit, style="TButton")
submit_button.grid(row=2, column=0, pady=10)
destroy_window=ttk.Button(frame,text="Exit",command=win_152.destroy,style="TButton")
destroy_window.grid(row=3, column=0)
win_152.mainloop()
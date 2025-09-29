
user = input("Enter your USSD code: ")
print("")

if user == "*301#":
    options = input(
        "..........\n"
        "1. Data\n"
        "2. Borrow\n"
        "3. Recharge\n"
        "4. Data Share\n"
        "5. Balance\n"
        "6. Data balance\n"
        "7. VAS\n"
        "8. Glo Cashtoken\n"
        "9. Glo App Offers\n"
        "10. Voice\n" 
        "11. More\n"
        "Please select an option: "
    )

    if options == "1":
        print("")
        opt = input(
            "..........\n"
            "1. Buy Data\n"
            "2. Gift Data\n"
            "3. Share Data\n"
            "4. Data Bal\n"
            "5. Voice Offers\n"
            "6. My-G Bundles\n"
            "7. App Offers- NEW\n"
            "8. Roaming Offers\n"
            "9. Always-ON Data Plans\n"
            "10. Borrow Credit\n"
            "Please select an option: "
        )
        if opt == "1":
            print("")
            opt1 = input(
                "..........\n"
                "1. Proceed (Auto-Renew)\n"
                "2. Proceed (One-off)\n"
                "Please select an option: "
            )
            if opt1 == "1":
                print("")
                opt2 = input(
                    "..........\n"
                    "1. Daily and Weekly\n"
                    "2. Monthly\n"      
                    "3. Mega Plans\n"      
                    "4. Super Mega Plans\n"  
                    "5. Special Data Offer\n"
                    "6. Social Bundles\n"
                    "7. Night & Weekend Plans\n"
                    "8. My-G Bundles\n"
                    "9. Always ON Bundles\n"
                    "Please select an option: "
                )
                if opt2 == "1":
                    print("")
                    opt3 = input(
                        "..........\n"
                        "1. \u20A6100 = 105MB 1 Day incl 5MB nite\n"
                        "2. \u20A6200 = 235MB 2 Days incl 25MB nite\n"
                        "3. \u20A6500 = 1.5GB 7 Days incl 1GB nite\n"
                        "4. \u20A650 = 45MB 1 Day incl 5MB nite\n"
                        "5. More Plans\n"
                        "Please select an option: "
                    )
                    if opt3 == "1":
                        print("You have successfully activated 105MB , valid for 1 Day which includes 5MB night")
                    elif opt3 == "2":
                        print("You have successfully activated 235MB, valid for 2 Days which includes 25MB night")
                    elif opt3 == "3":
                        print("You have successfully activated 1.5GB, valid for 7 Day which includes 1GB night")
                    elif opt3 == "4":
                        print("You have successfully activated 45MB, valid for 1 Day which includes 5MB night")
                    elif opt3 == "5":
                        print("")
                        opt4 = input(
                            "..........\n"
                            "1. \u20A6750 = 1.1GB 14 Days\n"
                            "2. \u20A61000 = 3.5GB 7 Days incl 2GB nite\n"
                            "3. \u20A62000 = 8.5GB 7 Days incl 2.5GB nite\n"
                            "4. \u20A65000 = 20.5GB 7 Days incl 2GB nite\n"
                            "Please select an option: "
                        )
                        if opt4 == "1":
                            print("You have successfully activated 1.1GB, valid for 14 Days")
                        elif opt4 == "2":
                            print("You have successfully activated 3.5GB, valid for 7 Days which includes 2GB night")
                        elif opt4 == "3":
                            print("You have successfully activated 8.5GB, valid for 7 Days which includes 2.5GB night")
                        elif opt4 == "4":
                            print("You have successfully activated 20.5GB, valid for 7 Days which includes 2GB night")
                        else:
                            print("Invalid option")
                    else:
                        print("Invalid option")
                elif opt2 == "2":
                    print("")
                    opt5 = input(
                        "..........\n"
                        "1. \u20A61000 = 2.6GB 30 Days incl 1.5GB nite\n"
                        "2. \u20A61500 = 5GB 30 Days incl 3GB nite\n"
                        "3. \u20A62000 = 6.15GB 30 Days incl 3GB nite\n"
                        "4. \u20A62500 = 7.25GB 30 Days incl 3GB nite\n"
                        "5. More Plans\n"
                        "Please select an option: "
                    )
                    if opt5 == "1":
                        print("You have successfully activated 2.6GB, valid for 30 Days which includes 1.5GB night")
                    elif opt5 == "2":
                       print("You have successfully activated 5GB, valid for 30 Days which includes 3GB night")
                    elif opt5 == "3":
                        print("You have successfully activated 6.15GB, valid for 30 Days which includes 3GB night")
                    elif opt5 == "4":
                       print("You have successfully activated 7.25GB, valid for 30 Days which includes 3GB night")
                    elif opt5 == "5":
                        print("")
                        opt6 = input(
                            "..........\n"
                            "1. \u20A63000 = 10GB 30 Days incl 2GB nite\n"
                            "2. \u20A64000 = 12.5GB 30 Days incl 2GB nite\n"
                            "3. \u20A65000 = 16GB 30 Days incl 2.5GB nite\n"
                            "4. \u20A66000 = 20.5GB 30 Days incl 2GB nite\n"
                            "88. Next\n"
                            "Please select an option: "
                        )
                        if opt6 == "1":
                            print("You have successfully activated 10GB, valid for 30 Days which includes 2GB night")
                        elif opt6 == "2":
                            print("You have successfully activated 12.5GB, valid for 30 Days which includes 2GB night")
                        elif opt6 == "3":
                            print("You have successfully activated 16GB, valid for 30 Days which includes 2.5GB night")
                        elif opt6 == "4":
                            print("You have successfully activated 20.5GB, valid for 30 Days which includes 2GB night")
                        elif opt6 == "88":
                            print("")
                            opt_088 = input(
                                "..........\n"
                                "1. \u20A68000 = 28GB for 30 Days incl 2GB nite"
                            )
                            if opt_088 == "1":
                                print("You have successfully activated 28GB, valid for 30 Days which includes 2GB night")
                            else:
                                print("Invalid option")
                        else:
                            print("Invalid option")
                    else:
                        print("Invalid option")
                elif opt2 == "3":
                    print("")
                    opt7 = input(
                        "..........\n"
                        "1. \u20A610000 = 38GB 30 Days incl 2GB nite\n"
                        "2. \u20A615000 = 64GB 30 Days incl 2GB nite\n"
                        "3. \u20A620000 = 107GB 30 Days incl 2GB nite\n"
                        "4. More Plans\n"
                        "Please select an option: "
                    )
                    if opt7 == "1":
                        print("You have successfully activated 38GB, valid for 30 Days which includes 2GB night")
                    elif opt7 == "2":
                        print("You have successfully activated 64GB, valid for 30 Days which includes 2GB night")
                    elif opt7 == "3":
                        print("You have successfully activated 107GB, valid for 30 Days which includes 2GB night")
                    elif opt7 == "4":
                        print("")
                        opt8 = input(
                            "..........\n"
                            "1. \u20A625000 = 135GB 30 Days\n"
                            "2. \u20A630000 = 165GB 30 Days\n"
                            "3. \u20A640000 = 220GB 30 Days\n"
                            "4. \u20A650000 = 310GB 60 Days\n"
                            "5. \u20A660000 = 355GB 90 Days\n"
                            "6. \u20A675000 = 475GB 90 Days\n"
                            "88. Next\n"
                            "Please select an option: "
                        )
                        if opt8 == "1":
                            print("You have successfully activated 135GB, valid for 30 Days")
                        elif opt8 == "2":
                            print("You have successfully activated 165GB, valid for 30 Days")
                        elif opt8 == "3":
                            print("You have successfully activated 220GB, valid for 30 Days")
                        elif opt8 == "4":
                            print("You have successfully activated 310GB, valid for 60 Days")
                        elif opt8 == "5":
                            print("You have successfully activated 355B, valid for 90 Days")
                        elif opt8 == "6":
                            print("You have successfully activated 475GB, valid for 90 Days")
                        elif opt8 == "88":
                            print("")
                            opt9 = input(
                                "..........\n"
                                "1. \u20A6150000 = 1000GB 1 Year\n"
                            )
                            if opt9 == "1":
                                print("You have successfully activated 1000GB, valid for 1 Year")
                            else:
                                print("Invalid option")
                        else:
                            print("Invalid option")
                    else:
                        print("Invalid option")
                elif opt2 == "4":
                    print("")
                    opt10 = input(
                        "..........\n"
                        "1. \u20A625000 = 135GB 30 Days\n"
                        "2. \u20A630000 = 165GB 30 Days\n"
                        "3. \u20A640000 = 220GB 30 Days\n"
                        "4. \u20A650000 = 310GB 60 Days\n"
                        "5. \u20A660000 = 355GB 90 Days\n"
                        "6. \u20A675000 = 475GB 90 Days\n"
                        "88. Next\n"
                        "Please select an option: "
                    )
                    if opt10 == "1":
                            print("You have successfully activated 135GB, valid for 30 Days")
                    elif opt10 == "2":
                            print("You have successfully activated 165GB, valid for 30 Days")
                    elif opt10 == "3":
                            print("You have successfully activated 220GB, valid for 30 Days")
                    elif opt10 == "4":
                            print("You have successfully activated 310GB, valid for 60 Days")
                    elif opt10 == "5":
                            print("You have successfully activated 355B, valid for 90 Days")
                    elif opt10 == "6":
                            print("You have successfully activated 475GB, valid for 90 Days")
                    elif opt10 == "88":
                        print("")
                        opt11 = input(
                            "..........\n"
                            "1. \u20A6150000 = 1000GB 1 Year\n"
                        )
                        if opt11 == "1":
                            print("You have successfully activated 1000GB, valid for 1 Year")
                        else:
                            print("Invalid option")
                    else:
                        print("Invalid option")
                elif opt2 == "5":
                    print("")
                    opt12 = input(
                        "..........\n"
                        "1. Special Plans\n"
                        "2. Campus Booster\n"
                        "3. Hourly Bundles\n"
                        "4. Betting Agent Plan\n"
                        "Please select an option: "
                    )
                    if opt12 == "1":
                        print("")
                        opt13 = input(
                            "..........\n"
                            "1. \u20A6350 = 1GB for 1 Day\n"
                            "2. \u20A6500 = 2GB for 1 Day incl 1GB nite\n"
                            "3. \u20A6600 = 3.55GB for 2 Days incl 2GB nite\n"
                            "4. \u20A61000 = 5.1GB for 2 Days incl 2GB nite\n"
                            "5. \u20A61500 = 5.9GB for 7 Days incl 2GB nite\n"
                            "Please select an option: "
                        )
                        if opt13 == "1":
                            print("You have successfully activated 1GB, valid for 1 day")
                        elif opt13 == "2":
                            print("You have successfully activated 2GB, valid for 1 day which includes 1GB night")
                        elif opt13 == "3":
                            print("You have successfully activated 3.55GB, valid for 2 days which includes 2GB night")
                        elif opt13 == "4":
                            print("You have successfully activated 5.1GB, valid for 2 days which includes 2GB night")
                        elif opt13 == "5":
                            print("You have successfully activated 5.9GB, valid for 7 days which includes 2GB night")
                        else:
                            print("Invalid option")
                    elif opt12 == "2":
                        print("")
                        opt14 = input(
                            "..........\n"
                            "1. \u20A6100 = 200MB for 1 Day\n"
                            "2. \u20A6200 = 445MB for 2 Days incl 25MB nite on campus\n"
                            "3. More\n"
                            "Please select an option: "
                        )
                        if opt14 == "1":
                            print("You have successfully activated 200MB, valid for 1 day")
                        elif opt14 == "2":
                            print("You have successfully activated 445MB, valid for 2 days which includes 25MB night")
                        elif opt14 == "3":
                            print("")
                            opt15 = input(
                                "..........\n"
                                "1. \u20A6500 = 2GB for 7 Days incl 1GB nite on campus\n"
                                "2. \u20A61000 = 4.2GB for 30 Days incl 2GB nite on campus\n"
                                "3. More\n"
                                "Please select an option: "
                            )
                            if opt15 == "1":
                                print("You have successfully activated 2GB, valid for 7 days which includes 1GB night")
                            elif opt15 == "2":
                                print("You have successfully activated 4.2GB, valid for 30 days which includes 2GB night")
                            elif opt15 == "3":
                                print("")
                                opt16 = input(
                                    "..........\n"
                                    "1. \u20A62000 = 9.8GB for 30 Days incl 3.5GB nite on campus\n"
                                    "2. \u20A65000 = 30GB for 30 Days incl 3GB nite on campus\n"
                                    "Please select an option: "
                                )
                                if opt16 == "1":
                                    print("You have successfully activated 9.8GB, valid for 30 days which includes 3.5GB night")
                                elif opt16 == "2":
                                    print("You have successfully activated 30GB, valid for 30 days which includes 3GB night")
                                else:
                                    print("Invalid option")
                            else:
                                print("Invalid option")
                        else:
                            print("Invalid option")
                    elif opt12 == "3":
                        print("")
                        opt17 = input(
                            "..........\n"
                            "1. \u20A6200 = 500MB for 1hr\n"
                            "2. \u20A6300 = 1GB for 2hrs\n"
                            "Please select an option: "
                        )
                        if opt17 == "1":
                            print("You have successfully activated 500MB, valid for 1hr")
                        elif opt17 == "2":
                            print("You have successfully activated 1GB, valid for 2hrs")
                        else:
                            print("Invalid option")
                    elif opt12 == "4":
                        print("")
                        opt18 = input(
                            "..........\n"
                            "1. \u20A61000 = 4GB for 30 Days\n"
                            "2. \u20A65000 = 30GB for 30 Days\n"
                            "3. \u20A610000 = 75GB for 30 Days\n"
                            "Please select an option: "
                        )
                        if opt18 == "1":
                            print("You have successfully activated 4GB, valid for 30 days")
                        elif opt18 == "2":
                            print("You have successfully activated 30GB, valid for 30 days")
                        elif opt18 == "3":
                            print("You have successfully activated 75GB, valid for 30 days")
                        else:
                            print("Invalid option")
                    else:
                        print("Invalid option")
                elif opt2 == "6":
                    print("")
                    opt19 = input(
                        "..........\n"
                        "1.Bundles for Whatsapp, Twitter, Facebook, Tiktok, Snapchat, Telegram, Instagram, Threads and GloTV\n"
                        "2.Bundles for Whatsapp, Tiktok, Instagram, Snapchat, Boomplay\n"
                        "Please select an option: "
                    )
                    if opt19 == "1":
                        print("")
                        opt20 = input(
                            "..........\n"
                            "1. \u20A650 = 135MB for 3 Days\n"
                            "2. \u20A6100 = 335MB for 7 Days\n"
                            "3. \u20A6300 = 1.1GB for 10 Days\n"
                            "4. \u20A6500 = 1.8GB for 15 Days\n"
                            "Please select an option: "
                        )
                        if opt20 == "1":
                            print("You have successfully activated 135MB, valid for 3 days")
                        elif opt20 == "2":
                            print("You have successfully activated 335MB, valid for 7 days")
                        elif opt20 == "3":
                            print("You have successfully activated 1.1GB, valid for 10 days")
                        elif opt20 == "4":
                            print("You have successfully activated 1.8GB, valid for 15 days")
                        else:
                            print("Invalid option")
                    elif opt19 == "2":
                        print("")
                        opt21 = input(
                            "..........\n"
                            "1. \u20A6100 = 300MB for 1 Day + 1hr\n"
                            "2. \u20A6300 = 1GB for 3 Days + 1hr\n"
                            "3. \u20A6500 = 1.5GB for 7 Days + 1hr\n"
                            "4. \u20A61000 = 3.5GB for 30 Days + 1hr\n"
                            "Please select an option: "
                        )
                        if opt21 == "1":
                            print("You have successfully activated 300MB, valid for 1 day + 1hr")
                        elif opt21 == "2":
                            print("You have successfully activated 1GB, valid for 3 days + 1hr")
                        elif opt21 == "3":
                            print("You have successfully activated 1.5GB, valid for 7 days + 1hr")
                        elif opt21 == "4":
                            print("You have successfully activated 3.5GB, valid for 30 days + 1hr")
                        else:
                            print("Invalid option")
                    else:
                        print("Invalid option")
                elif opt2 == "7":
                    print("")
                    opt22 = input(
                        "..........\n"
                        "1. \u20A660 = 350MB for 1 Day (12am-5am)\n"
                        "2. \u20A6120 = 750MB for 1 Day (12am-5am)\n"
                        "3. \u20A6200 = 875MB for 2 Days SAT-SUN\n"
                        "4. \u20A6500 = 2.5GB for 2 Days SAT-SUN\n"
                        "Please select an option: "
                    )
                    if opt22 == "1":
                        print("You have successfully activated 350MB, valid for 1 day (12am-5am)")
                    elif opt22 == "2":
                        print("You have successfully activated 750MB, valid for 1 day (12am-5am)")
                    elif opt22 == "3":
                        print("You have successfully activated 875MB, valid for 2 days (SAT-SUN)")
                    elif opt22 == "4":
                        print("You have successfully activated 2.5GB, valid for 2 days (SAT-SUN)")
                    else:
                        print("Invalid option")
                elif opt2 == "8":
                    print("")
                    opt23 = input(
                        "..........\n"
                        "Apps: WahtsApp, TikTok, Insta, Boomplay, Snapchat"
                        "1. \u20A6100 = 300MB for 1 Day + 1hr\n"
                        "2. \u20A6300 = 1GB for 3 Days + 1hr\n"
                        "3. \u20A6500 = 1.5GB for 7 Days + 1hr\n"
                        "4. \u20A61000 = 3.5GB for 30 Days + 1hr\n"
                        "Please select an option: "
                    )
                    if opt23 == "1":
                        print("You have successfully activated 300MB, valid for 1 day + 1hr")
                    elif opt23 == "2":
                        print("You have successfully activated 1GB, valid for 3 days + 1hr")
                    elif opt23 == "3":
                        print("You have successfully activated 1.5GB, valid for 7 days + 1hr")
                    elif opt23 == "4":
                        print("You have successfully activated 3.5GB, valid for 30 days + 1hr")
                    else:
                        print("Invalid option")
                elif opt2 == "9":
                    print("")
                    opt24 = input(
                        "..........\n"
                        "1. \u20A62000 = 6GB (Daily 410MB) for 15 Days\n"
                        "2. \u20A63500 = 15GB (Daily 500MB) for 30 Days\n"
                        "3. \u20A65000 = 30GB (Daily 1GB) for 30 Days\n"
                        "4. \u20A67000 = 45GB (Daily 1.5GB) for 30 Days\n"
                        "Please select an option: "
                    )
                    if opt24 == "1":
                        print("You have successfully activated 6GB (Daily 410MB), valid for 15 days")
                    elif opt24 == "2":
                        print("You have successfully activated 15GB (Daily 500MB), valid for 30 days")
                    elif opt24 == "3":
                        print("You have successfully activated 30GB (Daily 1GB), valid for 30 days")
                    elif opt24 == "4":
                        print("You have successfully activated 45GB (Daily 1.5GB), valid for 30 days")
                    else:
                        print("Invalid option")
                else:
                    print("Invalid option")
            elif opt1 == "2":
                print("")
                opt25 = input(
                    "..........\n"
                    "1. Daily and Weekly\n"
                    "2. Monthly\n"      
                    "3. Mega Plans\n"      
                    "4. Super Mega Plans\n"  
                    "5. Special Data Offer\n"
                    "6. Social Bundles\n"
                    "7. Night & Weekend Plans\n"
                    "8. My-G Bundles\n"
                    "9. Always ON Bundles\n"
                    "Please select an option: "
                )
                if opt25 == "1":
                    print("")
                    opt26 = input(
                        "..........\n"
                        "1. \u20A6100 = 105MB 1 Day incl 5MB nite\n"
                        "2. \u20A6200 = 235MB 2 Days incl 25MB nite\n"
                        "3. \u20A6500 = 1.5GB 7 Days incl 1GB nite\n"
                        "4. \u20A650 = 45MB 1 Day incl 5MB nite\n"
                        "5. More Plans\n"
                        "Please select an option: "
                    )
                    if opt26 == "1":
                        print("You have successfully activated 105MB , valid for 1 Day which includes 5MB night")
                    elif opt26 == "2":
                        print("You have successfully activated 235MB, valid for 2 Days which includes 25MB night")
                    elif opt26 == "3":
                        print("You have successfully activated 1.5GB, valid for 7 Day which includes 1GB night")
                    elif opt26 == "4":
                        print("You have successfully activated 45MB, valid for 1 Day which includes 5MB night")
                    elif opt26 == "5":
                        print("")
                        opt27 = input(
                            "..........\n"
                            "1. \u20A6750 = 1.1GB 14 Days\n"
                            "2. \u20A61000 = 3.5GB 7 Days incl 2GB nite\n"
                            "3. \u20A62000 = 8.5GB 7 Days incl 2.5GB nite\n"
                            "4. \u20A65000 = 20.5GB 7 Days incl 2GB nite\n"
                            "Please select an option: "
                        )
                        if opt27 == "1":
                            print("You have successfully activated 1.1GB, valid for 14 Days")
                        elif opt27 == "2":
                            print("You have successfully activated 3.5GB, valid for 7 Days which includes 2GB night")
                        elif opt27 == "3":
                            print("You have successfully activated 8.5GB, valid for 7 Days which includes 2.5GB night")
                        elif opt27 == "4":
                            print("You have successfully activated 20.5GB, valid for 7 Days which includes 2GB night")
                        else:
                            print("Invalid option")
                elif opt25 == "2":
                    print("")
                    opt28 = input(
                        "..........\n"
                        "1. \u20A61000 = 2.6GB 30 Days incl 1.5GB nite\n"
                        "2. \u20A61500 = 5GB 30 Days incl 3GB nite\n"
                        "3. \u20A62000 = 6.15GB 30 Days incl 3GB nite\n"
                        "4. \u20A62500 = 7.25GB 30 Days incl 3GB nite\n"
                        "5. More Plans\n"
                        "Please select an option: "
                    )
                    if opt28 == "1":
                        print("You have successfully activated 2.6GB, valid for 30 Days which includes 1.5GB night")
                    elif opt28 == "2":
                       print("You have successfully activated 5GB, valid for 30 Days which includes 3GB night")
                    elif opt28 == "3":
                        print("You have successfully activated 6.15GB, valid for 30 Days which includes 3GB night")
                    elif opt28 == "4":
                       print("You have successfully activated 7.25GB, valid for 30 Days which includes 3GB night")
                    elif opt28 == "5":
                        print("")
                        opt29 = input(
                            "..........\n"
                            "1. \u20A63000 = 10GB 30 Days incl 2GB nite\n"
                            "2. \u20A64000 = 12.5GB 30 Days incl 2GB nite\n"
                            "3. \u20A65000 = 16GB 30 Days incl 2.5GB nite\n"
                            "4. \u20A66000 = 20.5GB 30 Days incl 2GB nite\n"
                            "88. Next\n"
                            "Please select an option: "
                        )
                        if opt29== "1":
                            print("You have successfully activated 10GB, valid for 30 Days which includes 2GB night")
                        elif opt29 == "2":
                            print("You have successfully activated 12.5GB, valid for 30 Days which includes 2GB night")
                        elif opt29 == "3":
                            print("You have successfully activated 16GB, valid for 30 Days which includes 2.5GB night")
                        elif opt29 == "4":
                            print("You have successfully activated 20.5GB, valid for 30 Days which includes 2GB night")
                        elif opt29 == "88":
                            print("")
                            opt_089 = input(
                                "..........\n"
                                "1. \u20A68000 = 28GB for 30 Days incl 2GB nite"
                            )
                            if opt_089 == "1":
                                print("You have successfully activated 28GB, valid for 30 Days which includes 2GB night")
                            else:
                                print("Invalid option")
                        else:
                            print("Invalid option")
                    else:
                        print("Invalid option")
                elif opt25 == "3":
                    print("")
                    opt30 = input(
                        "..........\n"
                        "1. \u20A610000 = 38GB 30 Days incl 2GB nite\n"
                        "2. \u20A615000 = 64GB 30 Days incl 2GB nite\n"
                        "3. \u20A620000 = 107GB 30 Days incl 2GB nite\n"
                        "4. More Plans\n"
                        "Please select an option: "
                    )
                    if opt30 == "1":
                        print("You have successfully activated 38GB, valid for 30 Days which includes 2GB night")
                    elif opt30 == "2":
                        print("You have successfully activated 64GB, valid for 30 Days which includes 2GB night")
                    elif opt30 == "3":
                        print("You have successfully activated 107GB, valid for 30 Days which includes 2GB night")
                    elif opt30 == "4":
                        print("")
                        opt31 = input(
                            "..........\n"
                            "1. \u20A625000 = 135GB 30 Days\n"
                            "2. \u20A630000 = 165GB 30 Days\n"
                            "3. \u20A640000 = 220GB 30 Days\n"
                            "4. \u20A650000 = 310GB 60 Days\n"
                            "5. \u20A660000 = 355GB 90 Days\n"
                            "6. \u20A675000 = 475GB 90 Days\n"
                            "88. Next\n"
                            "Please select an option: "
                        )
                        if opt31 == "1":
                            print("You have successfully activated 135GB, valid for 30 Days")
                        elif opt31 == "2":
                            print("You have successfully activated 165GB, valid for 30 Days")
                        elif opt31 == "3":
                            print("You have successfully activated 220GB, valid for 30 Days")
                        elif opt31 == "4":
                            print("You have successfully activated 310GB, valid for 60 Days")
                        elif opt31 == "5":
                            print("You have successfully activated 355B, valid for 90 Days")
                        elif opt31 == "6":
                            print("You have successfully activated 475GB, valid for 90 Days")
                        elif opt31 == "88":
                            print("")
                            opt32 = input(
                                "..........\n"
                                "1. \u20A6150000 = 1000GB 1 Year\n"
                            )
                            if opt32 == "1":
                                print("You have successfully activated 1000GB, valid for 1 Year")
                            else:
                                print("Invalid option")
                        else:
                            print("Invalid option")
                    else:
                        print("Invalid option")
                elif opt25 == "4":
                    print("")
                    opt33 = input(
                        "..........\n"
                        "1. \u20A625000 = 135GB 30 Days\n"
                        "2. \u20A630000 = 165GB 30 Days\n"
                        "3. \u20A640000 = 220GB 30 Days\n"
                        "4. \u20A650000 = 310GB 60 Days\n"
                        "5. \u20A660000 = 355GB 90 Days\n"
                        "6. \u20A675000 = 475GB 90 Days\n"
                        "88. Next\n"
                        "Please select an option: "
                    )
                    if opt33 == "1":
                            print("You have successfully activated 135GB, valid for 30 Days")
                    elif opt33 == "2":
                            print("You have successfully activated 165GB, valid for 30 Days")
                    elif opt33 == "3":
                            print("You have successfully activated 220GB, valid for 30 Days")
                    elif opt33 == "4":
                            print("You have successfully activated 310GB, valid for 60 Days")
                    elif opt33 == "5":
                            print("You have successfully activated 355B, valid for 90 Days")
                    elif opt33 == "6":
                            print("You have successfully activated 475GB, valid for 90 Days")
                    elif opt33 == "88":
                        print("")
                        opt34 = input(
                            "..........\n"
                            "1. \u20A6150000 = 1000GB 1 Year\n"
                        )
                        if opt34 == "1":
                            print("You have successfully activated 1000GB, valid for 1 Year")
                        else:
                            print("Invalid option")
                    else:
                        print("Invalid option")
                elif opt25 == "5":
                    print("")
                    opt36 = input(
                        "..........\n"
                        "1. Special Plans\n"
                        "2. Campus Booster\n"
                        "3. Hourly Bundles\n"
                        "4. Betting Agent Plan\n"
                        "Please select an option: "
                    )
                    if opt36 == "1":
                        print("")
                        opt37 = input(
                            "..........\n"
                            "1. \u20A6350 = 1GB for 1 Day\n"
                            "2. \u20A6500 = 2GB for 1 Day incl 1GB nite\n"
                            "3. \u20A6600 = 3.55GB for 2 Days incl 2GB nite\n"
                            "4. \u20A61000 = 5.1GB for 2 Days incl 2GB nite\n"
                            "5. \u20A61500 = 5.9GB for 7 Days incl 2GB nite\n"
                            "Please select an option: "
                        )
                        if opt37 == "1":
                            print("You have successfully activated 1GB, valid for 1 day")
                        elif opt37 == "2":
                            print("You have successfully activated 2GB, valid for 1 day which includes 1GB night")
                        elif opt37 == "3":
                            print("You have successfully activated 3.55GB, valid for 2 days which includes 2GB night")
                        elif opt37 == "4":
                            print("You have successfully activated 5.1GB, valid for 2 days which includes 2GB night")
                        elif opt37 == "5":
                            print("You have successfully activated 5.9GB, valid for 7 days which includes 2GB night")
                        else:
                            print("Invalid option")
                    elif opt36 == "2":
                        print("")
                        opt38 = input(
                            "..........\n"
                            "1. \u20A6100 = 200MB for 1 Day\n"
                            "2. \u20A6200 = 445MB for 2 Days incl 25MB nite on campus\n"
                            "3. More option\n"
                            "Please select an option: "
                        )
                        if opt38 == "1":
                            print("You have successfully activated 200MB, valid for 1 day")
                        elif opt38 == "2":
                            print("You have successfully activated 445MB, valid for 2 days which includes 25MB night")
                        elif opt38 == "3":
                            print("")
                            opt39 = input(
                                "..........\n"
                                "1. \u20A6500 = 2GB for 7 Days incl 1GB nite on campus\n"
                                "2. \u20A61000 = 4.2GB for 30 Days incl 2GB nite on campus\n"
                                "3. More option\n"
                                "Please select an option: "
                            )
                            if opt39 == "1":
                                print("You have successfully activated 2GB, valid for 7 days which includes 1GB night")
                            elif opt39 == "2":
                                print("You have successfully activated 4.2GB, valid for 30 days which includes 2GB night")
                            elif opt39 == "3":
                                print("")
                                opt40 = input(
                                    "..........\n"
                                    "1. \u20A62000 = 9.8GB for 30 Days incl 3.5GB nite on campus\n"
                                    "2. \u20A65000 = 30GB for 30 Days incl 3GB nite on campus\n"
                                    "Please select an option: "
                                )
                                if opt40 == "1":
                                    print("You have successfully activated 9.8GB, valid for 30 days which includes 3.5GB night")
                                elif opt40 == "2":
                                    print("You have successfully activated 30GB, valid for 30 days which includes 3GB night")
                                else:
                                    print("Invalid option")
                            else:
                                print("Invalid option")
                        else:
                            print("Invalid option")
                    elif opt36 == "3":
                        print("")
                        opt41 = input(
                            "..........\n"
                            "1.\u20A6200 = 500MB for 1hr\n"
                            "2.\u20A6300 = 1GB for 2hrs\n"
                            "Please select an option: "
                        )
                        if opt41 == "1":
                            print("You have successfully activated 500MB, valid for 1hr")
                        elif opt41 == "2":
                            print("You have successfully activated 1GB, valid for 2hrs")
                        else:
                            print("Invalid option")
                    elif opt36 == "4":
                        print("")
                        opt42 = input(
                            "..........\n"
                            "1. \u20A61000 = 4GB for 30 Days\n"
                            "2. \u20A65000 = 30GB for 30 Days\n"
                            "3. \u20A610000 = 75GB for 30 Days\n"
                            "Please select an option: "
                        )
                        if opt42 == "1":
                            print("You have successfully activated 4GB, valid for 30 days")
                        elif opt42 == "2":
                            print("You have successfully activated 30GB, valid for 30 days")
                        elif opt42 == "3":
                            print("You have successfully activated 75GB, valid for 30 days")
                        else:
                            print("Invalid option")
                    else:
                        print("Invalid option")
                elif opt25 == "6":
                    print("")
                    opt43 = input(
                        "..........\n"
                        "1.Bundles for Whatsapp, Twitter, Facebook, Tiktok, Snapchat, Telegram, Instagram, Threads and GloTV\n"
                        "2.Bundles for Whatsapp, Tiktok, Instagram, Snapchat, Boomplay\n"
                        "Please select an option: "
                    )
                    if opt43 == "1":
                        print("")
                        opt44 = input(
                            "..........\n"
                            "1. \u20A650 = 135MB for 3 Days\n"
                            "2. \u20A6100 = 335MB for 7 Days\n"
                            "3. \u20A6300 = 1.1GB for 10 Days\n"
                            "4. \u20A6500 = 1.8GB for 15 Days\n"
                            "Please select an option: "
                        )
                        if opt44 == "1":
                            print("You have successfully activated 135MB, valid for 3 days")
                        elif opt44 == "2":
                            print("You have successfully activated 335MB, valid for 7 days")
                        elif opt44 == "3":
                            print("You have successfully activated 1.1GB, valid for 10 days")
                        elif opt44 == "4":
                            print("You have successfully activated 1.8GB, valid for 15 days")
                        else:
                            print("Invalid option")
                    elif opt43 == "2":
                        print("")
                        opt45 = input(
                            "..........\n"
                            "1. \u20A6100 = 300MB for 1 Day + 1hr\n"
                            "2. \u20A6300 = 1GB for 3 Days + 1hr\n"
                            "3. \u20A6500 = 1.5GB for 7 Days + 1hr\n"
                            "4. \u20A61000 = 3.5GB for 30 Days + 1hr\n"
                            "Please select an option: "
                        )
                        if opt45 == "1":
                            print("You have successfully activated 300MB, valid for 1 day + 1hr")
                        elif opt45 == "2":
                            print("You have successfully activated 1GB, valid for 3 days + 1hr")
                        elif opt45 == "3":
                            print("You have successfully activated 1.5GB, valid for 7 days + 1hr")
                        elif opt45 == "4":
                            print("You have successfully activated 3.5GB, valid for 30 days + 1hr")
                        else:
                            print("Invalid option")
                    else:
                        print("Invalid option")
                elif opt25 == "7":
                    print("")
                    opt47 = input(
                        "..........\n"
                        "1. \u20A660 = 350MB for 1 Day (12am-5am)\n"
                        "2. \u20A6120 = 750MB for 1 Day (12am-5am)\n"
                        "3. \u20A6200 = 875MB for 2 Days SAT-SUN\n"
                        "4. \u20A6500 = 2.5GB for 2 Days SAT-SUN\n"
                        "Please select an option: "
                    )
                    if opt47 == "1":
                        print("You have successfully activated 350MB, valid for 1 day (12am-5am)")
                    elif opt47 == "2":
                        print("You have successfully activated 750MB, valid for 1 day (12am-5am)")
                    elif opt47 == "3":
                        print("You have successfully activated 875MB, valid for 2 days (SAT-SUN)")
                    elif opt47 == "4":
                        print("You have successfully activated 2.5GB, valid for 2 days (SAT-SUN)")
                    else:
                        print("Invalid option")
                elif opt25 == "8":
                    print("")
                    opt48 = input(
                        "..........\n"
                        "Apps: WhatsApp, TikTok, Insta, Boomplay, Snapchat\n"
                        "1. \u20A6100 = 300MB for 1 Day + 1hr\n"
                        "2. \u20A6300 = 1GB for 3 Days + 1hr\n"
                        "3. \u20A6500 = 1.5GB for 7 Days + 1hr\n"
                        "4. \u20A61000 = 3.5GB for 30 Days + 1hr\n"
                        "Please select an option: "
                    )
                    if opt48 == "1":
                        print("You have successfully activated 300MB, valid for 1 day + 1hr")
                    elif opt48 == "2":
                        print("You have successfully activated 1GB, valid for 3 days + 1hr")
                    elif opt48 == "3":
                        print("You have successfully activated 1.5GB, valid for 7 days + 1hr")
                    elif opt48 == "4":
                        print("You have successfully activated 3.5GB, valid for 30 days + 1hr")
                    else:
                        print("Invalid option")
                elif opt25 == "9":
                    print("")
                    opt49 = input(
                        "..........\n"
                        "1. \u20A62000 = 6GB (Daily 410MB) for 15 Days\n"
                        "2. \u20A63500 = 15GB (Daily 500MB) for 30 Days\n"
                        "3. \u20A65000 = 30GB (Daily 1GB) for 30 Days\n"
                        "4. \u20A67000 = 45GB (Daily 1.5GB) for 30 Days\n"
                        "Please select an option: "
                    )
                    if opt49 == "1":
                        print("You have successfully activated 6GB (Daily 410MB), valid for 15 days")
                    elif opt49 == "2":
                        print("You have successfully activated 15GB (Daily 500MB), valid for 30 days")
                    elif opt49 == "3":
                        print("You have successfully activated 30GB (Daily 1GB), valid for 30 days")
                    elif opt49 == "4":
                        print("You have successfully activated 45GB (Daily 1.5GB), valid for 30 days")
                    else:
                        print("Invalid option")
                else:
                    print("Invalid option")
            else:
                print("Invalid option")
        elif opt == "2":
            print("")
            cha1 = input(
                "..........\n"
                "1. Daily-Weekly Plans\n"
                "2. Monthly Plans\n"      
                "3. Mega Plans\n"      
                "4. Super Mega Plans\n"  
                "5. Special Data Offer\n"
                "6. Social Bundles\n"
                "7. Night & Weekend Plans\n"
                "8. Always ON Bundles\n"
                "Please select an option: "
            )
            if cha1 == "1":
                print("")
                cha4 = input(
                    "..........\n"
                    "1. \u20A6100 = 105MB 1 Day incl 5MB nite\n"
                    "2. \u20A6200 = 235MB 2 Days incl 25MB nite\n"
                    "3. \u20A6500 = 1.5GB 7 Days incl 1GB nite\n"
                    "4. \u20A650 = 45MB 1 Day incl 5MB nite\n"
                    "5. More Plans\n"
                    "Please select an option: "
                )
                tel = input("Enter Giftee Number (Glo Line): ")
                if cha4 == "1":
                    if len(tel) == 11 and tel.isnumeric() and (tel.startswith("070") or tel.startswith("080") or tel.startswith("081") or tel.startswith("090") or tel.startswith("091")):
                        print(f"You have successfully credited {tel} with 105MB, which is valid for 1 Day and includes 5MB night")
                    else:
                        print("Invalid phone number")
                elif cha4 == "2":
                    if len(tel) == 11 and tel.isnumeric() and (tel.startswith("070") or tel.startswith("080") or tel.startswith("081") or tel.startswith("090") or tel.startswith("091")):
                        print(f"You have successfully credited {tel} with 235MB, which is valid for 2 Days and includes 25MB night")
                    else:
                        print("Invalid phone number")
                elif cha4 == "3":
                    if len(tel) == 11 and tel.isnumeric() and (tel.startswith("070") or tel.startswith("080") or tel.startswith("081") or tel.startswith("090") or tel.startswith("091")):
                        print(f"You have successfully credited {tel} with 1.5GB, which is valid for 7 Days and includes 1GB night")
                    else:
                        print("Invalid phone number")
                elif cha4 == "4":
                    if len(tel) == 11 and tel.isnumeric() and (tel.startswith("070") or tel.startswith("080") or tel.startswith("081") or tel.startswith("090") or tel.startswith("091")):
                        print(f"You have successfully credited {tel} with 45MB, which is valid for 1 Day and includes 5MB night")
                    else:
                        print("Invalid phone number")
                elif cha4 == "5":
                    print("")
                    cha5 = input(
                        "..........\n"
                        "1. \u20A6750 = 1.1GB 14 Days\n"
                        "2. \u20A61000 = 3.5GB 7 Days incl 2GB nite\n"
                        "3. \u20A62000 = 8.5GB 7 Days incl 2.5GB nite\n"
                        "4. \u20A65000 = 20.5GB 7 Days incl 2GB nite\n"
                        "Please select an option: "
                    )
                    if cha5 == "1":
                        if len(tel) == 11 and tel.isnumeric() and (tel.startswith("070") or tel.startswith("080") or tel.startswith("081") or tel.startswith("090") or tel.startswith("091")):
                            print(f"You have successfully credited {tel} with 1.1GB, which is valid for 14 Days")
                        else:
                            print("Invalid phone number")
                    elif cha5 == "2":
                        if len(tel) == 11 and tel.isnumeric() and (tel.startswith("070") or tel.startswith("080") or tel.startswith("081") or tel.startswith("090") or tel.startswith("091")):
                            print(f"You have successfully credited {tel} with 3.5GB, which is valid for 7 Days and includes 2GB night")
                        else:
                            print("Invalid phone number")
                    elif cha5 == "3":
                        if len(tel) == 11 and tel.isnumeric() and (tel.startswith("070") or tel.startswith("080") or tel.startswith("081") or tel.startswith("090") or tel.startswith("091")):
                            print(f"You have successfully credited {tel} with 8.5GB, which is valid for 7 Days and includes 2.5GB night")
                        else:
                            print("Invalid phone number")
                    elif cha5 == "4":
                        if len(tel) == 11 and tel.isnumeric() and (tel.startswith("070") or tel.startswith("080") or tel.startswith("081") or tel.startswith("090") or tel.startswith("091")):
                            print(f"You have successfully credited {tel} with 20.5GB, which is valid for 7 Days and includes 2GB night")
                        else:
                            print("Invalid phone number")
                    else:
                        print("Invalid option")
                else:
                    print("Invalid option")
            elif cha1 == "2":
                print("")
                cha6 = input(
                    "..........\n"
                    "1. \u20A61000 = 2.6GB 30 Days incl 1.5GB nite\n"
                    "2. \u20A61500 = 5GB 30 Days incl 3GB nite\n"
                    "3. \u20A62000 = 6.15GB 30 Days incl 3GB nite\n"
                    "4. \u20A62500 = 7.25GB 30 Days incl 3GB nite\n"
                    "5. More Plans\n"
                    "Please select an option: "
                )
                tel1 = input("Enter Giftee Number (Glo Line): ")
                if cha6 == "1":
                    if len(tel1) == 11 and tel1.isnumeric() and (tel1.startswith("070") or tel1.startswith("080") or tel1.startswith("081") or tel1.startswith("090") or tel1.startswith("091")):
                        print(f"You have successfully credited {tel1} with 2.66GB, which is valid for 30 Days and includes 1.5GB night")
                    else:
                        print("Invalid phone number")
                elif cha6 == "2":
                    if len(tel1) == 11 and tel1.isnumeric() and (tel1.startswith("070") or tel1.startswith("080") or tel1.startswith("081") or tel1.startswith("090") or tel1.startswith("091")):
                        print(f"You have successfully credited {tel1} with 5GB, which is valid for 30 Days and includes 3GB night")
                    else:
                        print("Invalid phone number")
                elif cha6 == "3":
                    if len(tel1) == 11 and tel1.isnumeric() and (tel1.startswith("070") or tel1.startswith("080") or tel1.startswith("081") or tel1.startswith("090") or tel1.startswith("091")):
                        print(f"You have successfully credited {tel1} with 6.15GB, which is valid for 30 Days and includes 3GB night")
                    else:
                        print("Invalid phone number")
                elif cha6 == "4":
                    if len(tel1) == 11 and tel1.isnumeric() and (tel1.startswith("070") or tel1.startswith("080") or tel1.startswith("081") or tel1.startswith("090") or tel1.startswith("091")):
                        print(f"You have successfully credited {tel1} with 7.25GB, which is valid for 30 Days and includes 3GB night")
                    else:
                        print("Invalid phone number")
                elif cha6 == "5":
                    print("")
                    cha7 = input(
                        "..........\n"
                        "1. \u20A63000 = 10GB 30 Days incl 2GB nite\n"
                        "2. \u20A64000 = 12.5GB 30 Days incl 2GB nite\n"
                        "3. \u20A65000 = 16GB 30 Days incl 2.5GB nite\n"
                        "4. \u20A66000 = 20.5GB 30 Days incl 2GB nite\n"
                        "88. Next\n"
                        "Please select an option: "
                    )
                    if cha7 == "1":
                        if len(tel1) == 11 and tel1.isnumeric() and (tel1.startswith("070") or tel1.startswith("080") or tel1.startswith("081") or tel1.startswith("090") or tel1.startswith("091")):
                            print(f"You have successfully credited {tel1} with 10GB, which is valid for 30 Days and includes 2GB night")
                        else:
                            print("Invalid phone number")
                    elif cha7 == "2":
                        if len(tel1) == 11 and tel1.isnumeric() and (tel1.startswith("070") or tel1.startswith("080") or tel1.startswith("081") or tel1.startswith("090") or tel1.startswith("091")):
                            print(f"You have successfully credited {tel1} with 12.5GB, which is valid for 30 Days and includes 2GB night")
                        else:
                            print("Invalid phone number")
                    elif cha7 == "3":
                        if len(tel1) == 11 and tel1.isnumeric() and (tel1.startswith("070") or tel1.startswith("080") or tel1.startswith("081") or tel1.startswith("090") or tel1.startswith("091")):
                            print(f"You have successfully credited {tel1} with 16GB, which is valid for 30 Days and includes 2.5GB night")
                        else:
                            print("Invalid phone number")
                    elif cha7 == "4":
                        if len(tel1) == 11 and tel1.isnumeric() and (tel1.startswith("070") or tel1.startswith("080") or tel1.startswith("081") or tel1.startswith("090") or tel1.startswith("091")):
                            print(f"You have successfully credited {tel1} with 20.5GB, which is valid for 30 Days and includes 2GB night")
                        else:
                            print("Invalid phone number")
                    elif cha7 == "88":
                        print("")
                        cha8 = input(
                            "..........\n"
                            "1. \u20A68000 = 28GB for 30 Days incl 2GB nite"
                        )
                        if cha8 == "1":
                            if len(tel1) == 11 and tel1.isnumeric() and (tel1.startswith("070") or tel1.startswith("080") or tel1.startswith("081") or tel1.startswith("090") or tel1.startswith("091")):
                                print(f"You have successfully credited {tel1} with 28GB, which is valid for 30 Days and includes 2GB night")
                            else:
                                print("Invalid phone number")
                        else:
                                print("Invalid option")
                    else:
                        print("Invalid option")
                else:
                    print("Invalid option")
            elif cha1 == "3":
                print("")
                cha9 = input(
                    "..........\n"
                    "1. \u20A610000 = 38GB 30 Days incl 2GB nite\n"
                    "2. \u20A615000 = 64GB 30 Days incl 1GB nite\n"
                    "3. \u20A620000 = 107GB 30 Days incl 2GB nite\n"
                    "4. More Plans\n"
                    "Please select an option: "
                )
                tel2 = input("Enter Giftee Number (Glo Line): ")
                if cha9 == "1":
                    if len(tel2) == 11 and tel2.isnumeric() and (tel2.startswith("070") or tel2.startswith("080") or tel2.startswith("081") or tel2.startswith("090") or tel2.startswith("091")):
                        print(f"You have successfully credited {tel2} with 38GB, which is valid for 30 Days and includes 2GB night")
                    else:
                        print("Invalid phone number")
                elif cha9 == "2":
                    if len(tel2) == 11 and tel2.isnumeric() and (tel2.startswith("070") or tel2.startswith("080") or tel2.startswith("081") or tel2.startswith("090") or tel2.startswith("091")):
                        print(f"You have successfully credited {tel2} with 64GB, which is valid for 30 Days and includes 1GB night")
                    else:
                        print("Invalid phone number")
                elif cha9 == "3":
                    if len(tel2) == 11 and tel2.isnumeric() and (tel2.startswith("070") or tel2.startswith("080") or tel2.startswith("081") or tel2.startswith("090") or tel2.startswith("091")):
                        print(f"You have successfully credited {tel2} with 107GB, which is valid for 30 Days and includes 2GB night")
                    else:
                        print("Invalid phone number")
                elif cha9 == "4":
                    print("")
                    cha10 = input(
                        "..........\n"
                        "1. \u20A625000 = 135GB 30 Days\n"
                        "2. \u20A630000 = 165GB 30 Days\n"
                        "3. \u20A640000 = 220GB 30 Days\n"
                        "4. \u20A650000 = 310GB 60 Days\n"
                        "5. \u20A660000 = 355GB 90 Days\n"
                        "6. \u20A675000 = 475GB 90 Days\n"
                        "7. \u20A6150000 = 1000GB 1 Year\n"
                        "Please select an option: "
                    )
                    if cha10 == "1":
                        if len(tel2) == 11 and tel2.isnumeric() and (tel2.startswith("070") or tel2.startswith("080") or tel2.startswith("081") or tel2.startswith("090") or tel2.startswith("091")):
                            print(f"You have successfully credited {tel2} with 135GB, which is valid for 30 Days")
                        else:
                            print("Invalid phone number")
                    elif cha10 == "2":
                        if len(tel2) == 11 and tel2.isnumeric() and (tel2.startswith("070") or tel2.startswith("080") or tel2.startswith("081") or tel2.startswith("090") or tel2.startswith("091")):
                            print(f"You have successfully credited {tel2} with 165GB, which is valid for 30 Days")
                        else:
                            print("Invalid phone number")
                    elif cha10 == "3":
                        if len(tel2) == 11 and tel2.isnumeric() and (tel2.startswith("070") or tel2.startswith("080") or tel2.startswith("081") or tel2.startswith("090") or tel2.startswith("091")):
                            print(f"You have successfully credited {tel2} with 220GB, which is valid for 30 Days")
                        else:
                            print("Invalid phone number")
                    elif cha10 == "4":
                        if len(tel2) == 11 and tel2.isnumeric() and (tel2.startswith("070") or tel2.startswith("080") or tel2.startswith("081") or tel2.startswith("090") or tel2.startswith("091")):
                            print(f"You have successfully credited {tel2} with 310GB, which is valid for 60 Days")
                        else:
                            print("Invalid phone number")
                    elif cha10 == "5":
                        if len(tel2) == 11 and tel2.isnumeric() and (tel2.startswith("070") or tel2.startswith("080") or tel2.startswith("081") or tel2.startswith("090") or tel2.startswith("091")):
                            print(f"You have successfully credited {tel2} with 355GB, which is valid for 90 Days")
                        else:
                            print("Invalid phone number")
                    elif cha10 == "6":
                        if len(tel2) == 11 and tel2.isnumeric() and (tel2.startswith("070") or tel2.startswith("080") or tel2.startswith("081") or tel2.startswith("090") or tel2.startswith("091")):
                            print(f"You have successfully credited {tel2} with 475GB, which is valid for 90 Days")
                        else:
                            print("Invalid phone number")
                    elif cha10 == "7":
                        if len(tel2) == 11 and tel2.isnumeric() and (tel2.startswith("070") or tel2.startswith("080") or tel2.startswith("081") or tel2.startswith("090") or tel2.startswith("091")):
                            print(f"You have successfully credited {tel2} with 1000GB, which is valid for 1 Year")
                        else:
                            print("Invalid phone number")
                    else:
                        print("Invalid option")
                else:
                    print("Invalid option")
            elif cha1 == "4":
                print("")
                cha11 = input(
                    "..........\n"
                    "1. \u20A625000 = 135GB 30 Days\n"
                    "2. \u20A630000 = 165GB 30 Days\n"
                    "3. \u20A640000 = 220GB 30 Days\n"
                    "4. \u20A650000 = 310GB 60 Days\n"
                    "5. \u20A660000 = 355GB 90 Days\n"
                    "6. \u20A675000 = 475GB 90 Days\n"
                    "7. \u20A6150000 = 1000GB 1 Year\n"
                    "Please select an option: "
                )
                tel4 = input("Enter Giftee Number (Glo Line): ")
                if cha11 == "1":
                    if len(tel4) == 11 and tel4.isnumeric() and (tel4.startswith("070") or tel4.startswith("080") or tel4.startswith("081") or tel4.startswith("090") or tel4.startswith("091")):
                        print(f"You have successfully credited {tel4} with 135GB, which is valid for 30 Days")
                    else:
                        print("Invalid phone number")
                elif cha11 == "2":
                    if len(tel4) == 11 and tel4.isnumeric() and (tel4.startswith("070") or tel4.startswith("080") or tel4.startswith("081") or tel4.startswith("090") or tel4.startswith("091")):
                        print(f"You have successfully credited {tel4} with 165GB, which is valid for 30 Days")
                    else:
                        print("Invalid phone number")
                elif cha11 == "3":
                    if len(tel4) == 11 and tel4.isnumeric() and (tel4.startswith("070") or tel4.startswith("080") or tel4.startswith("081") or tel4.startswith("090") or tel4.startswith("091")):
                        print(f"You have successfully credited {tel4} with 220GB, which is valid for 30 Days")
                    else:
                        print("Invalid phone number")
                elif cha11 == "4":
                    if len(tel4) == 11 and tel4.isnumeric() and (tel4.startswith("070") or tel4.startswith("080") or tel4.startswith("081") or tel4.startswith("090") or tel4.startswith("091")):
                        print(f"You have successfully credited {tel4} with 310GB, which is valid for 60 Days")
                    else:
                        print("Invalid phone number")
                elif cha11 == "5":
                    if len(tel4) == 11 and tel4.isnumeric() and (tel4.startswith("070") or tel4.startswith("080") or tel4.startswith("081") or tel4.startswith("090") or tel4.startswith("091")):
                        print(f"You have successfully credited {tel4} with 355GB, which is valid for 90 Days")
                    else:
                        print("Invalid phone number")
                elif cha11 == "6":
                    if len(tel4) == 11 and tel4.isnumeric() and (tel4.startswith("070") or tel4.startswith("080") or tel4.startswith("081") or tel4.startswith("090") or tel4.startswith("091")):
                        print(f"You have successfully credited {tel4} with 475GB, which is valid for 90 Days")
                    else:
                        print("Invalid phone number")
                elif cha11 == "7":
                    if len(tel4) == 11 and tel4.isnumeric() and (tel4.startswith("070") or tel4.startswith("080") or tel4.startswith("081") or tel4.startswith("090") or tel4.startswith("091")):
                        print(f"You have successfully credited {tel4} with 1000GB, which is valid for 1 Year")
                    else:
                        print("Invalid phone number")
                else:
                        print("Invalid option")
            elif cha1 == "5":
                print("")
                cha12 = input(
                    "..........\n"
                    "1. Special Plans\n"
                    "2. Campus Booster\n"
                    "3. Hourly Bundles\n"
                    "4. Betting Agent Plan\n"
                    "Please select an option: "
                )
                tel5 = input("Enter Giftee Number (Glo Line): ")
                if cha12 == "1":
                    print("")
                    cha13 = input(
                        "..........\n"
                        "1. \u20A6350 = 1GB for 1 Day\n"
                        "2. \u20A6500 = 2GB for 1 Day incl 1GB nite\n"
                        "3. \u20A6600 = 3.55GB for 2 Days incl 2GB nite\n"
                        "4. \u20A61000 = 5.1GB for 2 Days incl 2GB nite\n"
                        "5. \u20A61500 = 5.9GB for 7 Days incl 2GB nite\n"
                        "Please select an option: "
                    )
                    if cha13 == "1":
                        if len(tel5) == 11 and tel5.isnumeric() and (tel5.startswith("070") or tel5.startswith("080") or tel5.startswith("081") or tel5.startswith("090") or tel5.startswith("091")):
                            print(f"You have successfully credited {tel5} with 1GB, which is valid for 1 Day")
                        else:
                            print("Invalid phone number")
                    elif cha13 == "2":
                        if len(tel5) == 11 and tel5.isnumeric() and (tel5.startswith("070") or tel5.startswith("080") or tel5.startswith("081") or tel5.startswith("090") or tel5.startswith("091")):
                            print(f"You have successfully credited {tel5} with 2GB, which is valid for 1 Day and includes 1GB night")
                        else:
                            print("Invalid phone number")
                    elif cha13 == "3":
                        if len(tel5) == 11 and tel5.isnumeric() and (tel5.startswith("070") or tel5.startswith("080") or tel5.startswith("081") or tel5.startswith("090") or tel5.startswith("091")):
                            print(f"You have successfully credited {tel5} with 3.55GB, which is valid for 2 Days and includes 2GB night")
                        else:
                            print("Invalid phone number")
                    elif cha13 == "4":
                        if len(tel5) == 11 and tel5.isnumeric() and (tel5.startswith("070") or tel5.startswith("080") or tel5.startswith("081") or tel5.startswith("090") or tel5.startswith("091")):
                            print(f"You have successfully credited {tel5} with 5.1GB, which is valid for 2 Days and includes 2GB night")
                        else:
                            print("Invalid phone number")
                    elif cha13 == "5":
                        if len(tel5) == 11 and tel5.isnumeric() and (tel5.startswith("070") or tel5.startswith("080") or tel5.startswith("081") or tel5.startswith("090") or tel5.startswith("091")):
                            print(f"You have successfully credited {tel5} with 5.9GB, which is valid for 7 Days and includes 2GB night")
                        else:
                            print("Invalid phone number")
                    else:
                        print("Invalid option")
                elif cha12 == "2":
                    print("")
                    cha14 = input(
                        "..........\n"
                        "1. \u20A6100 = 200MB for 1 Day\n"
                        "2. \u20A6200 = 445MB for 2 Days incl 25MB nite on campus\n"
                        "3. More option\n"
                        "Please select an option: "
                    )
                    if cha14 == "1":
                        if len(tel5) == 11 and tel5.isnumeric() and (tel5.startswith("070") or tel5.startswith("080") or tel5.startswith("081") or tel5.startswith("090") or tel5.startswith("091")):
                            print(f"You have successfully credited {tel5} with 200MB, which is valid for 1 Days")
                        else:
                            print("Invalid phone number")
                    elif cha14 == "2":
                        if len(tel5) == 11 and tel5.isnumeric() and (tel5.startswith("070") or tel5.startswith("080") or tel5.startswith("081") or tel5.startswith("090") or tel5.startswith("091")):
                            print(f"You have successfully credited {tel5} with 445MB, which is valid for 2 Days")
                        else:
                            print("Invalid phone number")
                    elif cha14 == "3":
                        print("")
                        cha15 = input(
                            "..........\n"
                            "1. \u20A6500 = 2GB for 7 Days incl 1GB nite on campus\n"
                            "2. \u20A61000 = 4.2GB for 30 Days incl 2GB nite on campus\n"
                            "3. More option\n"
                            "Please select an option: "
                        )
                        if cha15 == "1":
                            if len(tel5) == 11 and tel5.isnumeric() and (tel5.startswith("070") or tel5.startswith("080") or tel5.startswith("081") or tel5.startswith("090") or tel5.startswith("091")):
                                print(f"You have successfully credited {tel5} with 2GB, which is valid for 7 Days which includes 1GB night")
                            else:
                                print("Invalid phone number")
                        elif cha15 == "2":
                            if len(tel5) == 11 and tel5.isnumeric() and (tel5.startswith("070") or tel5.startswith("080") or tel5.startswith("081") or tel5.startswith("090") or tel5.startswith("091")):
                                print(f"You have successfully credited {tel5} with 4.2GB, which is valid for 30 Days which includes 2GB night")
                            else:
                                print("Invalid phone number")
                        elif cha15 == "3":
                            print("")
                            cha16 = input(
                                "..........\n"
                                "1. \u20A62000 = 9.8GB for 30 Days incl 3.5GB nite on campus\n"
                                "2. \u20A65000 = 30GB for 30 Days incl 3GB nite on campus\n"
                                "Please select an option: "
                            )
                            if cha16 == "1":
                                if len(tel5) == 11 and tel5.isnumeric() and (tel5.startswith("070") or tel5.startswith("080") or tel5.startswith("081") or tel5.startswith("090") or tel5.startswith("091")):
                                    print(f"You have successfully credited {tel5} with 9.8GB, which is valid for 30 Days which includes 3.5GB night")
                                else:
                                    print("Invalid phone number")
                            elif cha16 == "2":
                                if len(tel5) == 11 and tel5.isnumeric() and (tel5.startswith("070") or tel5.startswith("080") or tel5.startswith("081") or tel5.startswith("090") or tel5.startswith("091")):
                                    print(f"You have successfully credited {tel5} with 30GB, which is valid for 30 Days which includes 3GB night")
                                else:
                                    print("Invalid phone number")
                            else:
                                print("Invalid option")
                        else:
                            print("Invalid option")
                    else:
                        print("Invalid option")
                elif cha12 == "3":
                    print("")
                    cha17 = input(
                        "..........\n"
                        "1.\u20A6200 = 500MB for 1hr\n"
                        "2.\u20A6300 = 1GB for 2hrs\n"
                        "Please select an option: "
                    )
                    if cha17 == "1":
                        if len(tel5) == 11 and tel5.isnumeric() and (tel5.startswith("070") or tel5.startswith("080") or tel5.startswith("081") or tel5.startswith("090") or tel5.startswith("091")):
                            print(f"You have successfully credited {tel5} with 500MB, which is valid for 1hr")
                        else:
                            print("Invalid phone number")
                    elif cha17 == "2":
                        if len(tel5) == 11 and tel5.isnumeric() and (tel5.startswith("070") or tel5.startswith("080") or tel5.startswith("081") or tel5.startswith("090") or tel5.startswith("091")):
                            print(f"You have successfully credited {tel5} with 1GB, which is valid for 2hrs")
                        else:
                            print("Invalid phone number")
                    else:
                        print("Invalid option")
                elif cha12 == "4":
                    print("")
                    cha18 = input(
                        "..........\n"
                        "1. \u20A61000 = 4GB for 30 Days\n"
                        "2. \u20A65000 = 30GB for 30 Days\n"
                        "3. \u20A610000 = 75GB for 30 Days\n"
                        "Please select an option: "
                    )
                    if cha18 == "1":
                        if len(tel5) == 11 and tel5.isnumeric() and (tel5.startswith("070") or tel5.startswith("080") or tel5.startswith("081") or tel5.startswith("090") or tel5.startswith("091")):
                            print(f"You have successfully credited {tel5} with 4GB, which is valid for 30 Days")
                        else:
                            print("Invalid phone number")
                    elif cha18 == "2":
                        if len(tel5) == 11 and tel5.isnumeric() and (tel5.startswith("070") or tel5.startswith("080") or tel5.startswith("081") or tel5.startswith("090") or tel5.startswith("091")):
                            print(f"You have successfully credited {tel5} with 30GB, which is valid for 30 Days")
                        else:
                            print("Invalid phone number")
                    elif cha18 == "3":
                        if len(tel5) == 11 and tel5.isnumeric() and (tel5.startswith("070") or tel5.startswith("080") or tel5.startswith("081") or tel5.startswith("090") or tel5.startswith("091")):
                            print(f"You have successfully credited {tel5} with 75GB, which is valid for 30 Days")
                        else:
                            print("Invalid phone number")
                    else:
                        print("Invalid option")
                else:
                    print("Invalid option")
            elif cha1 == "6":
                print("")
                cha19 = input(
                    "..........\n"
                    "1.Bundles for Whatsapp, Twitter, Facebook, Tiktok, Snapchat, Telegram, Instagram, Threads and GloTV\n"
                    "2.Bundles for Whatsapp, Tiktok, Instagram, Snapchat, Boomplay\n"
                    "Please select an option: "
                )
                tel6 = input("Enter Giftee Number (Glo Line): ")
                if cha19 == "1":
                    print("")
                    cha20 = input(
                        "..........\n"
                        "1. \u20A650 = 135MB for 3 Days\n"
                        "2. \u20A6100 = 335MB for 7 Days\n"
                        "3. \u20A6300 = 1.1GB for 10 Days\n"
                        "4. \u20A6500 = 1.8GB for 15 Days\n"
                        "Please select an option: "
                    )
                    if cha20 == "1":
                        if len(tel6) == 11 and tel6.isnumeric() and (tel6.startswith("070") or tel6.startswith("080") or tel6.startswith("081") or tel6.startswith("090") or tel6.startswith("091")):
                            print(f"You have successfully credited {tel6} with 135MB, which is valid for 3 Days")
                        else:
                            print("Invalid phone number")
                    elif cha20 == "2":
                        if len(tel6) == 11 and tel6.isnumeric() and (tel6.startswith("070") or tel6.startswith("080") or tel6.startswith("081") or tel6.startswith("090") or tel6.startswith("091")):
                            print(f"You have successfully credited {tel6} with 335MB, which is valid for 7 Days")
                        else:
                            print("Invalid phone number")
                    elif cha20 == "3":
                        if len(tel6) == 11 and tel6.isnumeric() and (tel6.startswith("070") or tel6.startswith("080") or tel6.startswith("081") or tel6.startswith("090") or tel6.startswith("091")):
                            print(f"You have successfully credited {tel6} with 1.1GB, which is valid for 10 Days")
                        else:
                            print("Invalid phone number")
                    elif cha20 == "4":
                        if len(tel6) == 11 and tel6.isnumeric() and (tel6.startswith("070") or tel6.startswith("080") or tel6.startswith("081") or tel6.startswith("090") or tel6.startswith("091")):
                            print(f"You have successfully credited {tel6} witH 1.8GB, which is valid for 15 Days")
                        else:
                            print("Invalid phone number")
                    else:
                        print("Invalid option")
                elif cha19 == "2":
                    print("")
                    cha21 = input(
                        "..........\n"
                        "1. \u20A6100 = 300MB for 1 Day + 1hr\n"
                        "2. \u20A6300 = 1GB for 3 Days + 1hr\n"
                        "3. \u20A6500 = 1.5GB for 7 Days + 1hr\n"
                        "4. \u20A61000 = 3.5GB for 30 Days + 1hr\n"
                        "Please select an option: "
                    )
                    if cha21 == "1":
                        if len(tel6) == 11 and tel6.isnumeric() and (tel6.startswith("070") or tel6.startswith("080") or tel6.startswith("081") or tel6.startswith("090") or tel6.startswith("091")):
                            print(f"You have successfully credited {tel6} with 300MB, which is valid for 1 Day + 1hr")
                        else:
                            print("Invalid phone number")
                    elif cha21 == "2":
                        if len(tel6) == 11 and tel6.isnumeric() and (tel6.startswith("070") or tel6.startswith("080") or tel6.startswith("081") or tel6.startswith("090") or tel6.startswith("091")):
                            print(f"You have successfully credited {tel6} with 1GB, which is valid for 3 Days + 1hr")
                        else:
                            print("Invalid phone number")
                    elif cha21 == "3":
                        if len(tel6) == 11 and tel6.isnumeric() and (tel6.startswith("070") or tel6.startswith("080") or tel6.startswith("081") or tel6.startswith("090") or tel6.startswith("091")):
                            print(f"You have successfully credited {tel6} with 1.5GB, which is valid for 7 Days + 1hr")
                        else:
                            print("Invalid phone number")
                    elif cha21 == "4":
                        if len(tel6) == 11 and tel6.isnumeric() and (tel6.startswith("070") or tel6.startswith("080") or tel6.startswith("081") or tel6.startswith("090") or tel6.startswith("091")):
                            print(f"You have successfully credited {tel6} with 3.5GB, which is valid for 30 Days + 1hr")
                        else:
                            print("Invalid phone number")
                    else:
                        print("Invalid option")
                else:
                    print("Invalid option")
            elif cha1 == "7":
                print("")
                cha22 = input(
                    "..........\n"
                    "1. \u20A660 = 350MB for 1 Day (12am-5am)\n"
                    "2. \u20A6120 = 750MB for 1 Day (12am-5am)\n"
                    "3. \u20A6200 = 875MB for 2 Days SAT-SUN\n"
                    "4. \u20A6500 = 2.5GB for 2 Days SAT-SUN\n"
                    "Please select an option: "
                )
                tel7 = input("Enter Giftee Number (Glo Line): ")
                if cha22 == "1":
                    if len(tel7) == 11 and tel7.isnumeric() and (tel7.startswith("070") or tel7.startswith("080") or tel7.startswith("081") or tel7.startswith("090") or tel7.startswith("091")):
                        print(f"You have successfully credited {tel7} with 350MB, which is valid for 1 Day (12am-5am)")
                    else:
                        print("Invalid phone number")
                elif cha22 == "2":
                    if len(tel7) == 11 and tel7.isnumeric() and (tel7.startswith("070") or tel7.startswith("080") or tel7.startswith("081") or tel7.startswith("090") or tel7.startswith("091")):
                        print(f"You have successfully credited {tel7} with 750MB, which is valid for 1 Day (12am-5am)")
                    else:
                        print("Invalid phone number")
                elif cha22 == "3":
                    if len(tel7) == 11 and tel7.isnumeric() and (tel7.startswith("070") or tel7.startswith("080") or tel7.startswith("081") or tel7.startswith("090") or tel7.startswith("091")):
                        print(f"You have successfully credited {tel7} with 875MB, which is valid for 2 Days SAT-SUN")
                    else:
                        print("Invalid phone number")
                elif cha22 == "4":
                    if len(tel7) == 11 and tel7.isnumeric() and (tel7.startswith("070") or tel7.startswith("080") or tel7.startswith("081") or tel7.startswith("090") or tel7.startswith("091")):
                        print(f"You have successfully credited {tel7} with 2.5GB, which is valid for 2 Days SAT-SUN")
                    else:
                        print("Invalid phone number")
                else:
                    print("Invalid option")
            elif cha1 == "8":
                print("")
                cha23 = input(
                    "..........\n"
                    "1. \u20A62000 = 6GB (Daily 410MB) for 15 Days\n"
                    "2. \u20A63500 = 15GB (Daily 500MB) for 30 Days\n"
                    "3. \u20A65000 = 30GB (Daily 1GB) for 30 Days\n"
                    "4. \u20A67000 = 45GB (Daily 1.5GB) for 30 Days\n"
                    "Please select an option: "
                )
                tel8 = input("Enter Giftee Number (Glo Line): ")
                if cha23 == "1":
                    if len(tel8) == 11 and tel8.isnumeric() and (tel8.startswith("070") or tel8.startswith("080") or tel8.startswith("081") or tel8.startswith("090") or tel8.startswith("091")):
                        print(f"You have successfully credited {tel8} with 6GB (Daily 410MB), which is valid for 15 Days")
                    else:
                        print("Invalid phone number")
                elif cha23 == "2":
                    if len(tel8) == 11 and tel8.isnumeric() and (tel8.startswith("070") or tel8.startswith("080") or tel8.startswith("081") or tel8.startswith("090") or tel8.startswith("091")):
                        print(f"You have successfully credited {tel8} with 15GB (Daily 500MB), which is valid for 30 Days")
                    else:
                        print("Invalid phone number")
                elif cha23 == "3":
                    if len(tel8) == 11 and tel8.isnumeric() and (tel8.startswith("070") or tel8.startswith("080") or tel8.startswith("081") or tel8.startswith("090") or tel8.startswith("091")):
                        print(f"You have successfully credited {tel8} with 30GB (Daily 1GB), which is valid for 30 Days")
                    else:
                        print("Invalid phone number")
                elif cha23 == "4":
                    if len(tel8) == 11 and tel8.isnumeric() and (tel8.startswith("070") or tel8.startswith("080") or tel8.startswith("081") or tel8.startswith("090") or tel8.startswith("091")):
                        print(f"You have successfully credited {tel8} with 45GB (Daily 1.5GB), which is valid for 30 Days")
                    else:
                        print("Invalid phone number")
                else:
                    print("Invalid option")
            else:
                print("Invalid option")
        elif opt == "3":
            print("")
            sel1 = input(
                "..........\n"
                "1. Share Data\n"
                "2. Unshare Data\n"
                "3. List of Shared Numbers\n"
                "4. Cancel Auto Renewal\n"
                "5. Manual Configuration Details\n"
                "6. Easy Share (Credit Share)\n"
                "Please select an option: "
            )
            if sel1 == "1":
                tel_1 = input("Please enter Glo subscriber number you want to share data with: ")
                if len(tel_1) == 11 and tel_1.isnumeric() and (tel_1.startswith("070") or tel_1.startswith("080") or tel_1.startswith("081") or tel_1.startswith("090") or tel_1.startswith("091")):
                    print(f"You are now sharing your subscription with {tel_1}")
                else:
                    print("Invalid phone number")
            elif sel1 == "2":
                tel_2 = input("Please enter Glo subscriber number you want to Unshare data with: ")
                if len(tel_2) == 11 and tel_2.isnumeric() and (tel_2.startswith("070") or tel_2.startswith("080") or tel_2.startswith("081") or tel_2.startswith("090") or tel_2.startswith("091")):
                    print(f"You have unshared your subscription with {tel_2}")
                else:
                    print("Invalid phone number")
            elif sel1 == "3":
                print("You don't have any number sharing your subscription")
            elif sel1 == "4":
                print("You have successfully canceled your auto renewal subscription")
            elif sel1 == "5":
                print("Please save the APN details under setting option in your handset. APN Name:gloflat UserName:flat Password:flat   ")
            elif sel1 == "6":
                print("To share airtime with other Glo Number, Pls dail *131*GloNumber*Amount*PIN# Default PIN:00000, Note: Easy Share is not available for Berekete Customers")
            else:
                print("Invalid option")
        elif opt == "4":
            print("You are on CGIFT_3GB, expires 22/07/2025 15:21, Your data balance is 2847MB and browsed for 272 Min")
        elif opt == "5":
            print("")
            sel2 = input(
                "..........\n"
                "1. My Tariff Plan\n"
                "2. Intl Call Offers\n"
                "3. Data Roaming Offers\n"
                "4. Glo Talk On\n"
                "5. Glo Super Talk\n"
                "6. Always On\n"
                "Please select an option: "
            )
            if sel2 == "1":
                print("")
                sel3 = input(
                    "..........\n"
                    "1. My Package\n"
                    "2. My Number\n"
                    "3. Friends and Family Number\n"
                    "4. Easy Share\n"
                )
                if sel3 == "1":
                    sel4 = input(
                        "1. To Know Your Package, Dial #100#\n"
                        "2. To Migrate to other profile, Dial *100#\n"
                    )
                    if sel4 == "1":
                        print("To Know Your Package, Dial #100#")
                    elif sel4 == "2":
                        print("To Migrate to other profile, Dial *100")
                    else:
                        print("")
                elif sel3 == "2":
                    print("Dear customer, to know your Glo Number, pleas dial *777#")
                elif sel3 == "3":
                    sel4 = input(
                        "1. To Manage Friends & Family, Dial *606*1#\n"
                        "2. View Freinds & Family list, Dial *170*50#\n"
                    )
                    if sel4 == "1":
                        print("To Manage Friends & Family, Dial *606*1#")
                    elif sel4 == "2":
                        print("View Freinds & Family list, Dial *170*50#")
                    else:
                        print("Invalid option")
                elif sel3 == "4":
                    print("Dear customer, for Me2U please dial *131*Phone Number*Amount*PIN#")
                else:
                    print("Invalid option")
            elif sel2 == "2":
                print("")
                sel6 = input(
                    "..........\n"
                    "1. \u20A6100 = 3 Min 1 Day\n"
                    "2. \u20A6200 = 7 Min 3 Days\n"
                    "3. \u20A6500 = 18 Min 10 Days\n"
                    "4. \u20A61000 = 37 Min 30 Days\n"
                    "5. List of 8 countries\n"
                    "6. Check IDD Pack Balance\n"
                    "Please select an option: "
                )
                if sel6 == "1":
                    print("You have successfully activated an international call offer, valid for 3 Min for a day")
                elif sel6 == "2":
                    print("You have successfully activated an international call offer, valid for 7 Min for 3 days")
                elif sel6 == "3":
                    print("You have successfully activated an international call offer, valid for 18 Min for 10 days")
                elif sel6 == "4":
                    print("You have successfully activated an international call offer, valid for 3 Min for a day")
                elif sel6 == "5":
                    print("USA, Canada, Bangladesh, Malaysia, Puerto Rico, Romania, Norway, Peru")
                elif sel6 == "6":
                    print("Dear Customer, you don't have a bundle. Kindly dial *777# to buy a bundle of your choice")
                else:
                    print("Invalid option")
            elif sel2 == "3":
                print("")
                sel7 = input(
                    "..........\n"
                    "1. \u20A62500 = 50MB 3 Days\n"
                    "2. \u20A65000 = 125MB 7 Days\n"
                    "3. \u20A610000 = 1GB 10 Days\n"
                    "4. \u20A625000 = 2.5GB 30 Days\n"
                    "5. \u20A650000 = 6GB 60 Days\n"
                    "6. List of countries & partners\n"
                    "Please select an option: "
                )
                if sel7 == "1":
                    print("You have successfully activated 50MB, valid for 3 days")
                elif sel7 == "2":
                    print("You have successfully activated 125MB, valid for 7 days")
                elif sel7 == "3":
                    print("You have successfully activated 1GB, valid for 10 days")
                elif sel7 == "4":
                    print("You have successfully activated 2.5GB, valid for 30 days")
                elif sel7 == "5":
                    print("You have successfully activated 6GB, valid for 60 days")
                elif sel7 == "6":
                    print("UAE - Etisalat, Ghana - Millicom. UK - H3G. USA - Tmobile. USA - AT&T. USA - Limitless. France - Orange.")
                    print("Saudi Arabia - Saudi Telecom, Kenya - Safaricom. Turkey - Avea. Italy - Telecom Italia. India - Vodafoneidea.")
                    print("South Africa - Telkcom. Netherlands - KPN. Switzerland Swisscom. Switzerland - Orange. Belgium - Mobistar.")
                    print("Poland - Polkomtel. Luxemborg - Orange. Sweden - Tel2. Cyprus - Areeba. Estonia - Tele2. Ireland - Meteor.")
                    print("Ireland - H3G. Malta - Salt. Srilanka - Hutchison. Srilanka - Etisalat. Hongkong - PCCW. Hongkong - H3G. ")
                    print("Iceland - Simmin. Liechteinstein - Salt. Indonesia - IND Telkomsel. Isreal - IL Pelephone. Macau - CTM. Iran - MCI.")
                    print("Sudan - Zain. Brazil - Claro. Dominican - Claro. Equador - Claro. Nicaragua - Claro. Peru - Claro. Puerto Rico - Claro")
                    print("Argentina - Claro. Andorra - Orange. Monaco - Orange. San Marino - TIM")
                else:
                    print("Invalid option")
            elif sel2 == "4":
                print("")
                sel8 = input(
                    "..........\n"
                    "Get 10 times value of all your recharges with GLO TALK ON. To migrate:\n"
                    "1. Glo Talk On\n"
                    "Please select an option: "
                )
                if sel8 == "1":
                    print("Sorry, the ussd command you sent is not valid")
                else:
                    print("Invalid option")
            elif sel2 == "5":
                print("")
                sel9 = input(
                    "..........\n"
                    "Get 10 times value of all your recharges with GLO SUPER TALK. To migrate:\n"
                    "1. Glo Super Talk\n"
                    "Please select an option: "
                )
                if sel9 == "1":
                    print("Sorry, the ussd command you sent is not valid")
                else:
                    print("Invalid option")
            elif sel2 == "6":
                print("Your request for ALWAYS ON subscription is being processed. Please dial #100# after 2hrs for confirmation.")
                print("A fee of \u20A6500 is charged for this service")
            else:
                print("Invalid option")
        elif opt == "6":
            print("")
            sel10 = input(
                "..........\n"
                "Apps: WahtsApp, TikTok, Insta, Boomplay, Snapchat\n"
                "1. \u20A6100 = 400MB for 1 Day + 1hr\n"
                "2. \u20A6300 = 1GB for 3 Days + 1hr\n"
                "3. \u20A6500 = 1.5GB for 7 Days + 1hr\n"
                "4. \u20A61000 = 3.5GB for 30 Days + 1hr\n"
                "Please select an option: "
            )
            if sel10 == "1":
                print("You have successfully activated 400MB, valid for 1 day + 1hr")
            elif sel10== "2":
                print("You have successfully activated 1GB, valid for 3 days + 1hr")
            elif sel10 == "3":
                print("You have successfully activated 1.5GB, valid for 7 days + 1hr")
            elif sel10 == "4":
                print("You have successfully activated 3.5GB, valid for 30 days + 1hr")
            else:
                print("Invalid option")
        elif opt == "7":
            print("")
            sel11 = input(
                "..........\n"
                "Exciting Offers Only On Glo Cafe App\n"
                "1. 100GB Bonus App\n"
                "2. Recharge Bonus - 100%\n"
                "3. 10% More On Data Plans\n"
                "4. App Only Special Data Bundles\n"
                "5. Enjoy Glo Cafe Offers!\n"
                "Please select an option: "
            )
            if sel11 == "1":
                print("Only For New Users: Download & Register Glo Cafe App & get 100GB Data (75GB instant)")
                print("+ 5GB for 5 Months) Hurry! Download the GLO CAFE App from App store")
            elif sel11 == "2":
                print("100% Recharge Bonus on Cafe: Get 100% Recharge Bonus Every Time on recharges done through")
                print("done through Glo Cafe App. Hurry! Download the GLO CAFE App from App store")
            elif sel11 == "3":
                print("10% Bonus Data: On Data Plans purchased through Glo Cafe App, Example: 300MB more")
                print("on \u20A62000 Bundle. Hurry! Download the GLO CAFE App from App store")
            elif sel11 == "4":
                print("Special Bundles: Avaliable Only On App, \u20A6200 = 300MB 1D, \u20A6300 = 1.5GB 1D, \u20A6500 = 2.5GB 2D,")
                print("\u20A62000 = 10GB 7D. Hurry! Download the GLO CAFE App from App store")
            elif sel11 == "5":
                print("100GB Bonus + 100% Recharge Bonus + 10% More Data + Special Data Bundles App Download")
                print("Links: Android:bit.ly/3zQUZRA, iOS:apple.co/3o60s4v")
            else:
                print("Invalid option")
        elif opt == "8":
            print("")
            sel12 = input(
                "..........\n"
                "1. Data Roaming Bundle\n"
                "2. Combo Roaming Bundle\n"
                "Please select an option: "
            )
            if sel12 == "1":
                print("")
                sel13 = input(
                    "..........\n"
                    "1. \u20A62500 = 50MB 3 Days\n"
                    "2. \u20A65000 = 125MB 7 Days\n"
                    "3. \u20A610000 = 1GB 10 Days\n"
                    "4. \u20A625000 = 2.5GB 30 Days\n"
                    "5. \u20A650000 = 6GB 60 Days\n"
                    "6. List of countries & partners\n"
                    "Please select an option: "
                )
                if sel13 == "1":
                    print("You have successfully activated 50MB, valid for 3 days")
                elif sel13 == "2":
                    print("You have successfully activated 125MB, valid for 7 days")
                elif sel13 == "3":
                    print("You have successfully activated 1GB, valid for 10 days")
                elif sel13 == "4":
                    print("You have successfully activated 2.5GB, valid for 30 days")
                elif sel13 == "5":
                    print("You have successfully activated 6GB, valid for 60 days")
                elif sel13 == "6":
                    print("UAE - Etisalat, Ghana - Millicom. UK - H3G. USA - Tmobile. USA - AT&T. USA - Limitless. France - Orange.")
                    print("Saudi Arabia - Saudi Telecom, Kenya - Safaricom. Turkey - Avea. Italy - Telecom Italia. India - Vodafoneidea.")
                    print("South Africa - Telkcom. Netherlands - KPN. Switzerland Swisscom. Switzerland - Orange. Belgium - Mobistar.")
                    print("Poland - Polkomtel. Luxemborg - Orange. Sweden - Tel2. Cyprus - Areeba. Estonia - Tele2. Ireland - Meteor.")
                    print("Ireland - H3G. Malta - Salt. Srilanka - Hutchison. Srilanka - Etisalat. Hongkong - PCCW. Hongkong - H3G. ")
                    print("Iceland - Simmin. Liechteinstein - Salt. Indonesia - IND Telkomsel. Isreal - IL Pelephone. Macau - CTM. Iran - MCI.")
                    print("Sudan - Zain. Brazil - Claro. Dominican - Claro. Equador - Claro. Nicaragua - Claro. Peru - Claro. Puerto Rico - Claro")
                    print("Argentina - Claro. Andorra - Orange. Monaco - Orange. San Marino - TIM")
                else:
                    print("Invalid option")
            elif sel12 == "2":
                print("")
                sel13 = input(
                    "..........\n"
                    "1. \u20A62500 = 5 Mins Voice + 50MB 1 Day\n"
                    "2. \u20A65000 = 10 Mins Voice + 100MB 2 Days\n"
                    "3. List of countries\n"
                    "Please select an option: "
                )
                if sel13 == "1":
                    print("You have successfully activated 50MB, valid for 1 day with 5 Mins Voice")
                elif sel13 == "2":
                    print("You have successfully activated 105MB, valid for 2 days with 10 Mins Voice")
                elif sel13 == "3":
                    print("Saudi Arabia - Saudi Telecom")
                else:
                    print("Invalid option")
            else:
                print("Invalid option")
        elif opt == "9":
            print("")
            sel14 = input(
                "..........\n"
                "1. \u20A62000 = 6GB (Daily 410MB) for 15 Days\n"
                "2. \u20A63500 = 15GB (Daily 500MB) for 30 Days\n"
                "3. \u20A65000 = 30GB (Daily 1GB) for 30 Days\n"
                "4. \u20A67000 = 45GB (Daily 1.5GB) for 30 Days\n"
                "Please select an option: "
            )
            if sel14 == "1":
                print("You have successfully activated 6GB (Daily 410MB), valid for 15 days")
            elif sel14 == "2":
                print("You have successfully activated 15GB (Daily 500MB), valid for 30 days")
            elif sel14 == "3":
                print("You have successfully activated 30GB (Daily 1GB), valid for 30 days")
            elif sel14 == "4":
                print("You have successfully activated 45GB (Daily 1.5GB), valid for 30 days")
            else:
                print("Invalid option")
        elif opt == "10":
            print("")
            sel15 = input(
                "..........\n"
                "Dear Customer, Welcome, you are eligible for \u20A650. Reply with\n"
                "1. My BMC Account\n"
                "2. Borrow Credit\n"
                "3. Borrow Data\n"
                "4. Borrow Credit for Others\n"
                "5. Borrow Data for Others\n"
                "Please select an option: "
            )
            if sel15 == "1":
                print("")
                sel16 = input(
                    "..........\n"
                    "1. Balance\n"
                    "2. Payment\n"
                    "3. Repay Loan\n"
                    "Please select an option: "
                )
                if sel16 == "1":
                    print("You have no advance airtime uncleared balance")
                elif sel16 == "2":
                    print("Connection problem or invalid MMI code")
                elif sel16 == "3":
                    print("Dear Customer, your repayment request is being processed")
                else:
                    print("Invalid option")
            elif sel15 == "2":
                print("")
                sel17 = input(
                    "..........\n"
                    "1. \u20A650\n"
                    "2. \u20A625\n"
                    "3. Help\n"
                    "4. Balance\n"
                    "Please select an option: "
                )
                if sel17 == "1":
                    print("You have successfully borrowed \u20A650")
                elif sel17 == "2":
                    print("You have successfully borrowed \u20A625")
                elif sel17 == "3":
                    print("Connection problem or invalid MMI code")
                elif sel17 == "4":
                    print("You have no advance airtime uncleared balance")
                else:
                    print("Invalid option")
            elif sel15 == "3":
                print("")
                sel18 = input(
                    "..........\n"
                    "You are eligible for \u20A650\n"
                    "1. \u20A650 = 40MB + 5MB\n"
                    "Please select an option:"
                )
                if sel18 == "1":
                    print("You have successfully borrowed 40MB + 5MB at \u20A650")
                else:
                    print("Invalid option")
            elif sel15 == "4":
                print("")
                sel19 = input(
                    "..........\n"
                    "1. \u20A650\n"
                    "2. \u20A625\n"
                    "3. Help\n"
                    "4. Balance\n"
                    "Please select an option: "
                )
                tel = input("Enter phone number of the recipient: ")
                if sel19 == "1":
                    if len(tel) == 11 and tel.isnumeric() and (tel.startswith("070") or tel.startswith("080") or tel.startswith("081") or tel.startswith("090") or tel.startswith("091")):
                        print(f"You have successfully credited {tel} with \u20A650")
                    else:
                        print("Invalid phone number")
                elif sel19 == "2":
                    if len(tel) == 11 and tel.isnumeric() and (tel.startswith("070") or tel.startswith("080") or tel.startswith("081") or tel.startswith("090") or tel.startswith("091")):
                        print(f"You have successfully credited {tel} with \u20A625")
                    else:
                        print("Invalid phone number")
                elif sel19 == "3":
                    print("Connection problem or invalid MMI code")
                elif sel19 == "4":
                    print("You have no advance airtime uncleared balance")
                else:
                    print("Invalid option")
            elif sel15 == "5":
                print("")
                sel20 = input(
                    "..........\n"
                    "You are eligible for \u20A650\n"
                    "1. \u20A650 = 40MB + 5MB\n"
                    "Please select an option:"
                )
                tel1 = input("Enter phone number of the recipient: ")
                if sel20 == "1":
                    if len(tel1) == 11 and tel1.isnumeric() and (tel1.startswith("070") or tel1.startswith("080") or tel1.startswith("081") or tel1.startswith("090") or tel1.startswith("091")):
                        print(f"You have successfully credited {tel1} with 40MB + 5MB at \u20A650")
                    else:
                        print("Invalid phone number")
            else:
                print("Invalid option")
        else:
            print("Invalid option")
    elif options == "2":
        print("")
        sel15 = input(
            "..........\n"
            "Dear Customer, Welcome, you are eligible for \u20A650. Reply with\n"
            "1. My BMC Account\n"
            "2. Borrow Credit\n"
            "3. Borrow Data\n"
            "4. Borrow Credit for Others\n"
            "5. Borrow Data for Others\n"
            "Please select an option: "
        )
        if sel15 == "1":
            print("")
            sel16 = input(
                "..........\n"
                "1. Balance\n"
                "2. Payment\n"
                "3. Repay Loan\n"
                "Please select an option: "
            )
            if sel16 == "1":
                print("You have no advance airtime uncleared balance")
            elif sel16 == "2":
                print("Connection problem or invalid MMI code")
            elif sel16 == "3":
                print("Dear Customer, your repayment request is being processed")
            else:
                print("Invalid option")
        elif sel15 == "2":
            print("")
            sel17 = input(
                "..........\n"
                "1. \u20A650\n"
                "2. \u20A625\n"
                "3. Help\n"
                "4. Balance\n"
                "Please select an option: "
            )
            if sel17 == "1":
                print("You have successfully borrowed \u20A650")
            elif sel17 == "2":
                print("You have successfully borrowed \u20A625")
            elif sel17 == "3":
                print("Connection problem or invalid MMI code")
            elif sel17 == "4":
                print("You have no advance airtime uncleared balance")
            else:
                print("Invalid option")
        elif sel15 == "3":
            print("")
            sel18 = input(
                "..........\n"
                "You are eligible for \u20A650\n"
                "1. \u20A650 = 40MB + 5MB\n"
                "Please select an option:"
            )
            if sel18 == "1":
                print("You have successfully borrowed 40MB + 5MB at \u20A650")
            else:
                print("Invalid option")
        elif sel15 == "4":
            print("")
            sel19 = input(
                "..........\n"
                "1. \u20A650\n"
                "2. \u20A625\n"
                "3. Help\n"
                "4. Balance\n"
                "Please select an option: "
            )
            tel = input("Enter phone number of the recipient: ")
            if sel19 == "1":
                if len(tel) == 11 and tel.isnumeric() and (tel.startswith("070") or tel.startswith("080") or tel.startswith("081") or tel.startswith("090") or tel.startswith("091")):
                    print(f"You have successfully credited {tel} with \u20A650")
                else:
                    print("Invalid phone number")
            elif sel19 == "2":
                if len(tel) == 11 and tel.isnumeric() and (tel.startswith("070") or tel.startswith("080") or tel.startswith("081") or tel.startswith("090") or tel.startswith("091")):
                    print(f"You have successfully credited {tel} with \u20A625")
                else:
                    print("Invalid phone number")
            elif sel19 == "3":
                print("Connection problem or invalid MMI code")
            elif sel19 == "4":
                print("You have no advance airtime uncleared balance")
            else:
                print("Invalid option")
        elif sel15 == "5":
            print("")
            sel20 = input(
                "..........\n"
                "You are eligible for \u20A650\n"
                "1. \u20A650 = 40MB + 5MB\n"
                "Please select an option:"
            )
            tel1 = input("Enter phone number of the recipient: ")
            if sel20 == "1":
                if len(tel1) == 11 and tel1.isnumeric() and (tel1.startswith("070") or tel1.startswith("080") or tel1.startswith("081") or tel1.startswith("090") or tel1.startswith("091")):
                    print(f"You have successfully credited {tel1} with 40MB + 5MB at \u20A650")
                else:
                    print("Invalid phone number")
        else:
            print("Invalid option")
    elif options == "3":
        print("Dear Customer, as per NCC directive, the airtime recharge code is now 311. To recharge dial *311*RechargePin#. Thanks!")
    elif options == "4":
        print("")
        sel1 = input(
            "..........\n"
            "1. Share Data\n"
            "2. Unshare Data\n"
            "3. List of Shared Numbers\n"
            "4. Cancel Auto Renewal\n"
            "5. Manual Configuration Details\n"
            "6. Easy Share (Credit Share)\n"
            "Please select an option: "
        )
        if sel1 == "1":
            tel_1 = input("Please enter Glo subscriber number you want to share data with: ")
            if len(tel_1) == 11 and tel_1.isnumeric() and (tel_1.startswith("070") or tel_1.startswith("080") or tel_1.startswith("081") or tel_1.startswith("090") or tel_1.startswith("091")):
                print(f"You are now sharing your subscription with {tel_1}")
            else:
                print("Invalid phone number")
        elif sel1 == "2":
            tel_2 = input("Please enter Glo subscriber number you want to Unshare data with: ")
            if len(tel_2) == 11 and tel_2.isnumeric() and (tel_2.startswith("070") or tel_2.startswith("080") or tel_2.startswith("081") or tel_2.startswith("090") or tel_2.startswith("091")):
                print(f"You have unshared your subscription with {tel_2}")
            else:
                print("Invalid phone number")
        elif sel1 == "3":
            print("You don't have any number sharing your subscription")
        elif sel1 == "4":
            print("You have successfully canceled your auto renewal subscription")
        elif sel1 == "5":
            print("Please save the APN details under setting option in your handset. APN Name:gloflat UserName:flat Password:flat   ")
        elif sel1 == "6":
            print("To share airtime with other Glo Number, Pls dail *131*GloNumber*Amount*PIN# Default PIN:00000, Note: Easy Share is not available for Berekete Customers")
        else:
            print("Invalid option")
    elif options == "5":
        print("")
        ans = input(
            "..........\n"
            "1. Main A/C Balance\n"
            "2. Bonus A/C Balance\n"
            "3. Post Paid A/C Balance: Dial *310#\n"
            "Please select an option: "
        )
        if ans == "1":
            print("Main balance is \u20A6100.88")
        elif ans == "2":
            print("Dear Customer, you don't have a bundle. Kindly dial *777# to buy a bundle of your choice")
        elif ans == "3":
            print("Sorry, the USSD command you sent is not valid")
        else:
            print("Invalid option")
    elif options == "6":
        print("You are on CGIFT_3GB, expires 22/07/2025 15:21, Your data balance is 2847MB and browsed for 272 Min")
    elif options == "7":
        print("")
        pol = input(
            "..........\n"
            "Welcome.\n"
            "1. Gaming Service\n"
            "2. Educational service\n"
            "3. Lottery\n"
            "4. Entertainment\n" 
            "5. Sports Service\n" 
            "6. Caller Tunes\n"
            "7. BMC\n"
            "8. Glo Cloud\n"
            "9. Unsubscribe\n"
            "Please select an option: "
        )
        if pol == "1":
            print("")
            pol1 = input(
                "..........\n"
                "1. Gaming Portal\n"
                "2. Gaming Tournament\n"
                "3. Edu games\n"
                "4. Game Box\n"
                "5. Games Play\n"
                "6. Glo Games Club\n"
                "7. Glo Kidjo TV\n"
                "8. Wazoo Play\n"
                "Please select an option: "
            )
            if pol1 == "1":
                print("")
                pol2 = input(
                    "..........\n"
                    "Welcome to gaming portal service\n"
                    "1. Daily Auto Pack @\u20A630\n"
                    "2. Daily one time pack @\u20A630\n"
                    "Please select a pack: "
                )
                if pol2 == "1":
                    print("You have successfully subscribed to the product")
                elif pol2 == "2":
                    print("You have successfully subscribed to the product")
                else:
                    print("Invalid option")
            elif pol1 == "2":
                print("")
                pol3 = input(
                    "..........\n"
                    "Welcome to gaming tournament services\n"
                    "1. Daily Auto @\u20A630\n"
                    "2. Weekly Auto @\u20A650\n"
                    "3. Monthly Pack @\u20A6200\n"
                    "4. Daily one time @\u20A620\n"
                    "5. Weekly one time @\u20A650\n"
                    "6. Monthly one time @\u20A6200\n"
                    "Please select a pack: "
                )
                if pol3 == "1":
                    print("You have successfully subscribed to the product")
                elif pol3 == "2":
                    print("You have successfully subscribed to the product")
                elif pol3 == "3":
                    print("You have successfully subscribed to the product")
                elif pol3 == "4":
                    print("You have successfully subscribed to the product")
                elif pol3 == "5":
                    print("You have successfully subscribed to the product")
                elif pol3 == "6":
                    print("You have successfully subscribed to the product")
                else:
                    print("Invalid option")
            elif pol1 == "3":
                print("")
                pol4 = input(
                    "..........\n"
                    "Welcome to Edu Games Services\n"
                    "1. Daily Auto @\u20A650\n"
                    "2. Weekly Auto @\u20A6100\n"
                    "3. Monthly Pack @\u20A6200\n"
                    "4. Daily one time @\u20A650\n"
                    "5. Weekly one time @\u20A6100\n"
                    "6. Monthly one time @\u20A6200\n"
                    "Please select a pack: "
                )
                if pol4 == "1":
                    print("You have successfully subscribed to the product")
                elif pol4 == "2":
                    print("You have successfully subscribed to the product")
                elif pol4 == "3":
                    print("You have successfully subscribed to the product")
                elif pol4 == "4":
                    print("You have successfully subscribed to the product")
                elif pol4 == "5":
                    print("You have successfully subscribed to the product")
                elif pol4 == "6":
                    print("You have successfully subscribed to the product")
                else:
                    print("Invalid option")
            elif pol1 == "4":
                print("")
                pol5 = input(
                    "..........\n"
                    "Welcome to Game Box Services\n"
                    "1. Daily Auto @\u20A615\n"
                    "2. Weekly Auto @\u20A655\n"
                    "3. Monthly Pack @\u20A6155\n"
                    "4. Daily one time @\u20A615\n"
                    "5. Weekly one time @\u20A655\n"
                    "6. Monthly one time @\u20A6155\n"
                    "Please select a pack: "
                )
                if pol5 == "1":
                    print("You have successfully subscribed to the product")
                elif pol5 == "2":
                    print("You have successfully subscribed to the product")
                elif pol5 == "3":
                    print("You have successfully subscribed to the product")
                elif pol5 == "4":
                    print("You have successfully subscribed to the product")
                elif pol5 == "5":
                    print("You have successfully subscribed to the product")
                elif pol5 == "6":
                    print("You have successfully subscribed to the product")
                else:
                    print("Invalid option")
            elif pol1 == "5":
                print("")
                pol6 = input(
                    "..........\n"
                    "Welcome to Games Play Services\n"
                    "1. Daily Auto @\u20A620\n"
                    "2. Weekly Auto @\u20A660\n"
                    "3. Monthly Pack @\u20A6150\n"
                    "4. Daily one time @\u20A620\n"
                    "5. Weekly one time @\u20A660\n"
                    "6. Monthly one time @\u20A6150\n"
                    "Please select a pack: "
                )
                if pol6 == "1":
                    print("You have successfully subscribed to the product")
                elif pol6 == "2":
                    print("You have successfully subscribed to the product")
                elif pol6 == "3":
                    print("You have successfully subscribed to the product")
                elif pol6 == "4":
                    print("You have successfully subscribed to the product")
                elif pol6 == "5":
                    print("You have successfully subscribed to the product")
                elif pol6 == "6":
                    print("You have successfully subscribed to the product")
                else:
                    print("Invalid option")
            elif pol1 == "6":
                print("")
                pol7 = input(
                    "..........\n"
                    "Welcome to Glo Games Club Services\n"
                    "1. Daily Pack @\u20A610\n"
                    "2. Weekly @\u20A650\n"
                    "3. Monthly Pack @\u20A6100\n"
                    "4. Unsubscribe\n"
                    "Please select a pack: "
                )
                if pol7 == "1":
                    print("You have successfully subscribed to the product")
                elif pol7 == "2":
                    print("You have successfully subscribed to the product")
                elif pol7 == "3":
                    print("You have successfully subscribed to the product")
                elif pol7 == "4":
                    print("You have successfully unsubscribed to this plan")
                else:
                    print("Invalid option")
            elif pol1 == "7":
                print("")
                pol8 = input(
                    "..........\n"
                    "Welcome to Glo Kidjo\n"
                    "1. Daily Auto @\u20A620\n"
                    "2. Weekly Auto @\u20A660\n"
                    "3. Monthly Auto @\u20A6150\n"
                    "4. Daily one time @\u20A620\n"
                    "5. Weekly one time @\u20A660\n"
                    "6. Monthly one time @\u20A6150\n"
                    "88. Next\n"
                    "Please select a pack: "
                )
                if pol8 == "1":
                    print("You have successfully subscribed to the product")
                elif pol8 == "2":
                    print("You have successfully subscribed to the product")
                elif pol8 == "3":
                    print("You have successfully subscribed to the product")
                elif pol8 == "4":
                    print("You have successfully subscribed to the product")
                elif pol8 == "5":
                    print("You have successfully subscribed to the product")
                elif pol8 == "6":
                    print("You have successfully subscribed to the product")
                elif pol8 == "88":
                    print("")
                    pol9 = input(
                        "..........\n"
                        "7. Unsubscribe\n"
                        "Please select an option: "
                    )
                    if pol9 == "7":
                       print("You have successfully unsubscribed to the plan")
                    else:
                        print("Invalid option")
                else:
                    print("Invalid option")
            elif pol1 == "8":
                print("")
                pol10 = input(
                    "..........\n"
                    "Welcome.\n"
                    "1. WAZOPLAY\n"
                    "2. SPIN4CASH\n"
                    "3. UNSUBSCRIBE\n"
                    "Please select an option: "
                )
                if pol10 == "1":
                    print("")
                    pol11 = input(
                        "..........\n"
                        "Welcome to WAZOPLAY\n"
                        "1. Daily Auto @\u20A6100\n"
                        "2. Weekly Auto @\u20A6200\n"
                        "3. Daily one time @\u20A6100\n"
                        "4. Weekly one time @\u20A6200\n"
                        "5. Monthly Auto @\u20A6500\n"
                        "88. Next\n"
                        "Please select a pack: "
                    )
                    if pol11 == "1":
                        print("You have successfully subscribed to the product")
                    elif pol11 == "2":
                        print("You have successfully subscribed to the product")
                    elif pol11 == "3":
                        print("You have successfully subscribed to the product")
                    elif pol11 == "4":
                        print("You have successfully subscribed to the product")
                    elif pol11 == "5":
                        print("You have successfully subscribed to the product")
                    elif pol11 == "88":
                        print("")
                        pol12 = input(
                            "..........\n"
                            "6. Monthly One time @\u20A6500\n"
                            "Please select an option: "
                        )
                        if pol12 == "6":
                            print("You have successfully subscribed to the product")
                        else:
                            print("Invalid option")
                    else:
                        print("Invalid option")
                elif pol10 == "2":
                    print("")
                    pol13 = input(
                        "..........\n"
                        "Welcome to SPIN4CASH\n"
                        "1. One Spin Daily Auto @\u20A650\n"
                        "2. Two Spin Daily Auto @\u20A6100\n"
                        "3. Five Spin Weekly Auto @\u20A6250\n"
                        "4. One Spin Daily one time @\u20A650\n"
                        "88. Next\n"
                        "Please select a pack: "
                    )
                    if pol13 == "1":
                        print("You have successfully subscribed to the product")
                    elif pol13 == "2":
                        print("You have successfully subscribed to the product")
                    elif pol13 == "3":
                        print("You have successfully subscribed to the product")
                    elif pol13 == "4":
                        print("You have successfully subscribed to the product")
                    elif pol13 == "88":
                        print("")
                        pol14 = input(
                            "..........\n"
                            "5. Two Spin Daily one time @\u20A6100\n"
                            "6. Five Spin Weekly one time @\u20A6250\n"
                            "7. Ten Spin Monthly one time @\u20A6500\n"
                            "Please select an option: "
                        )
                        if pol14 == "5":
                            print("You have successfully subscribed to the product")
                        elif pol14 == "6":
                            print("You have successfully subscribed to the product")
                        elif pol14 == "7":
                            print("You have successfully subscribed to the product")
                        else:
                            print("Invalid option")
                    else:
                        print("Invalid option")
                elif pol10 == "3":
                    print("")
                    pol15 = input(
                        "..........\n"
                        "1. WAZOPLAY\n"
                        "2. SPIN4CASH\n"
                        "Please select an option: "
                    )
                    if pol15 == "1":
                        print("")
                        pol16 = input(
                            "..........\n"
                            "Welcome to WAZOPLAY\n"
                            "1. Daily Auto @\u20A6100\n"
                            "2. Weekly Auto @\u20A6200\n"
                            "3. Daily one time @\u20A6100\n"
                            "4. Weekly one time @\u20A6200\n"
                            "5. Monthly Auto @\u20A6500\n"
                            "88. Next\n"
                            "Please select a pack: "
                        )
                        if pol16 == "1":
                            print("You have successfully unsubscribed to the product")
                        elif pol16 == "2":
                            print("You have successfully unsubscribed to the product")
                        elif pol16 == "3":
                            print("You have successfully unsubscribed to the product")
                        elif pol16 == "4":
                            print("You have successfully unsubscribed to the product")
                        elif pol16 == "5":
                            print("You have successfully unsubscribed to the product")
                        elif pol16 == "88":
                            print("")
                            pol17 = input(
                                "..........\n"
                                "6. Monthly One time @\u20A6500\n"
                                "Please select an option: "
                            )
                            if pol17 == "6":
                                print("You have successfully unsubscribed to the product")
                            else:
                                print("Invalid option")
                        else:
                            print("Invalid option")
                    elif pol15 == "2":
                        print("")
                        pol18 = input(
                            "..........\n"
                            "Welcome to SPIN4CASH\n"
                            "1. One Spin Daily Auto @\u20A650\n"
                            "2. Two Spin Daily Auto @\u20A6100\n"
                            "3. Five Spin Weekly Auto @\u20A6250\n"
                            "4. One Spin Daily one time @\u20A650\n"
                            "88. Next\n"
                            "Please select a pack: "
                        )
                        if pol18 == "1":
                            print("You have successfully unsubscribed to the product")
                        elif pol18 == "2":
                            print("You have successfully unsubscribed to the product")
                        elif pol18 == "3":
                            print("You have successfully unsubscribed to the product")
                        elif pol18 == "4":
                            print("You have successfully unsubscribed to the product")
                        elif pol18 == "88":
                            print("")
                            pol19 = input(
                                "..........\n"
                                "5. Two Spin Daily one time @\u20A6100\n"
                                "6. Five Spin Weekly one time @\u20A6250\n"
                                "7. Ten Spin Monthly one time @\u20A6500\n"
                                "Please select an option: "
                            )
                            if pol19 == "5":
                                print("You have successfully unsubscribed to the product")
                            elif pol19 == "6":
                                print("You have successfully unsubscribed to the product")
                            elif pol19 == "7":
                                print("You have successfully unsubscribed to the product")
                            else:
                                print("Invalid option")
                        else:
                            print("Invalid option")
                    else:
                        print("Invalid option")
                else:
                    print("Invalid option")
            else:
                print("Invalid option")
        elif pol == "2":
            print("")
            pol20 = input(
                "..........\n"
                "1. Language Learning - Busuu\n"
                "2. Edu Video\n"
                "Please select an option: "
            )
            if pol20 == "1":
                print("")
                pol21 = input(
                    "..........\n"
                    "Welcome to Busuu Language Learning Service\n"
                    "1. Daily Auto Pack @\u20A620\n"
                    "2. Weekly Auto Pack @\u20A6100\n"
                    "3. Daily one time pack @\u20A620\n"
                    "4. Weekly one time pack @\u20A6100\n"
                    "Please select an option: "
                )
                if pol21 == "1":
                    print("You have successfully subscribed to the product")
                elif pol21 == "2":
                    print("You have successfully subscribed to the product")
                elif pol21 == "3":
                    print("You have successfully subscribed to the product")
                elif pol21 == "4":
                    print("You have successfully subscribed to the product")
                else:
                    print("Invalid option")
            elif pol20 == "2":
                print("")
                pol22 = input(
                    "..........\n"
                    "Welcome to Edu. Video Service\n"
                    "1. Daily Auto @\u20A650\n"
                    "2. Weekly Auto @\u20A6100\n"
                    "3. Monthly Pack @\u20A6200\n"
                    "4. Daily one time @\u20A650\n"
                    "5. Weelkly one time @\u20A6100\n"
                    "88. Next\n"
                    "Please select a pack: "
                )
                if pol22 == "1":
                    print("You have successfully subscribed to the product")
                elif pol22 == "2":
                    print("You have successfully subscribed to the product")
                elif pol22 == "3":
                    print("You have successfully subscribed to the product")
                elif pol22 == "4":
                    print("You have successfully subscribed to the product")
                elif pol22 == "5":
                    print("You have successfully subscribed to the product")
                elif pol22 == "88":
                    print("")
                    pol23 = input(
                        "..........\n"
                        "6. Monthly One time @\u20A6200\n"
                        "Please select an option: "
                    )
                    if pol23 == "6":
                        print("You have successfully subscribed to the product")
                    else:
                        print("Invalid option")
            else:
                print("Invalid option")
        elif pol == "3":
            print("")
            pol24 = input(
                "..........\n"
                "1. Lucky Number\n"
                "2. Green Lotto\n"
                "3. Perfect 10\n"
                "4. Jolly Suite\n"
                "5. Africa Winner\n"
                "6. Zoom Lottery\n"
                "Please select an option: "
            )
            if pol24 == "1":
                print("")
                sel1 = input(
                    "..........\n"
                    "Welcome to Lucky Number Service\n"
                    "1. Lucky Number Economy: \u20A6150\n"
                    "2. Lucky Number Max: \u20A6200\n"
                    "3. Lucky Number Premium: \u20A6500\n"
                    "4. Unsubscribe\n"
                    "5. Draw Result\n"
                    "Please select an option: "
                )
                if sel1 == "1":
                    print("")
                    sel2 = input(
                        "..........\n"
                        "Thanks for choosing Lucky Number Economy @\u20A6150 daily\n"
                        "1. Auto Renewal\n"
                        "2. One-time or One-off\n"
                        "Please select an option: "
                    )
                    if sel2 == "1":
                        print("You have successfully activated lucky number economy @\u20A6150 at daily")
                    elif sel2 == "2":
                        print("You have successfully activated lucky number economy @\u20A6150 at daily")
                    else:
                        print("Invalid option")
                elif sel1 == "2":
                    print("")
                    sel3 = input(
                        "..........\n"
                        "Thanks for choosing Lucky Number Max @\u20A6200 daily\n"
                        "1. Auto Renewal\n"
                        "2. One-time or One-off\n"
                        "Please select an option: "
                    )
                    if sel3 == "1":
                        print("You have successfully activated lucky number max @\u20A6200 at daily")
                    elif sel3 == "2":
                        print("You have successfully activated lucky number max @\u20A6200 at daily")
                    else:
                        print("Invalid option")
                elif sel1 == "3":
                    print("")
                    sel3 = input(
                        "..........\n"
                        "Thanks for choosing Lucky Number Premium @\u20A6500 daily\n"
                        "1. Auto Renewal\n"
                        "2. One-time or One-off\n"
                        "Please select an option: "
                    )
                    if sel3 == "1":
                        print("You have successfully activated lucky number premium @\u20A6500 at daily")
                    elif sel3 == "2":
                        print("You have successfully activated lucky number premium @\u20A6500 at daily")
                    else:
                        print("Invalid option")
                elif sel1 == "4":
                    print("")
                    sel5 = input(
                        "..........\n"
                        "1. Lucky number Economy\n"
                        "2. Lucky number Max\n"
                        "3. Lucky number Premium\n"
                        "Please select a package: "
                    )
                    if sel5 == "1":
                        print("")
                        sel6 = input(
                            "..........\n"
                            "1. Lucky Number Economy Auto\n"
                            "2. Lucky Number Economy one time\n"
                            "Please select an option"
                        )
                        if sel6 == "1":
                            print("You have successfully unsubscribed from lucky number economy")
                        elif sel6 == "2":
                            print("You have successfully unsubscribed from lucky number economy")
                        else:
                            print("Invalid option")
                    elif sel5 == "2":
                        print("")
                        sel7 = input(
                            "..........\n"
                            "1. Lucky Number Max Auto\n"
                            "2. Lucky Number Max one time\n"
                            "Please select an option"
                        )
                        if sel7 == "1":
                            print("You have successfully unsubscribed from lucky number max")
                        elif sel7 == "2":
                            print("You have successfully unsubscribed from lucky number max")
                        else:
                            print("Invalid option")
                    elif sel5 == "3":
                        print("")
                        sel8 = input(
                            "..........\n"
                            "1. Lucky Number Premium Auto\n"
                            "2. Lucky Number Premium one time\n"
                            "Please select an option"
                        )
                        if sel8 == "1":
                            print("You have successfully unsubscribed from lucky number premium")
                        elif sel8 == "2":
                            print("You have successfully unsubscribed from lucky number premium")
                        else:
                            print("Invalid option")
                    else:
                        print("Invalid option")
                elif sel1 == "5":
                    print("Not available at the moment, please try again later")
                else:
                    print("Invalid option")
            elif pol24 == "2":
                print("")
                sel9 = input(
                    "..........\n"
                    "Green Lotto. I accept T&C by Playing/Subscribing\n"
                    "1. Economy \u20A6100\n"
                    "2. Premium \u20A6400\n"
                    "3. Daily Draw 11:9\n"
                    "4. Instant Draw Menu\n"
                    "5. Play 5/90\n"
                    "6. Scratch Game\n"
                    "7. Winning\n"
                    "88. Next\n"
                    "Please select an option: "
                )
                if sel9 == "1":
                    print("You have successfully subscribed for economy @\u20A6100")
                elif sel9 == "2":
                    print("You have successfully subscribed for premium @\u20A6400")
                elif sel9 == "3":
                    print("You have successfully subscribed for daily draw at 11:59 daily")
                elif sel9 == "4":
                    print("")
                    sel10 = input(
                        "..........\n"
                        "1. \u20A650\n"
                        "2. \u20A6100\n"
                        "Please select ticket amount: "
                    )
                    if sel10 == "1":
                        print("You have successfully activated instant draw @\u20A650")
                    elif sel10 == "2":
                        print("You have successfully activated instant draw @\u20A6100")
                    else:
                        print("Invalid option")
                elif sel9 == "5":
                    print("")
                    sel11 = input(
                        "..........\n"
                        "Today's Game:\n"
                        "1. FAAJI 5/90 09:00PM\n"
                        "2. CHAMPION 5/90 10:00PM\n"
                        "Please select an option: "
                    )
                    if sel11 == "1":
                        print("You have successfully activated FAAJI 5/90 @09:00PM")
                    elif sel11 == "2":
                        print("You have successfully activated CHAMPION 5/90 @10:00PM")
                    else:
                        print("Invalid option")
                elif sel9 == "6":
                    print("")
                    sel12 = input(
                        "..........\n"
                        "1. \u20A650\n"
                        "2. \u20A6100\n"
                        "Please select stake amount: "
                    )
                    if sel12 == "1":
                        print("You have successfully activated scratch gamne @\u20A650")
                    elif sel12 == "2":
                        print("You have successfully activated scratch game @\u20A6100")
                    else:
                        print("Invalid option")
                elif sel9 == "7":
                    print("There is no winning in your account")
                elif sel9 == "88":
                    print("")
                    sel13 = input(
                        "..........\n"
                        "8. Add Bank\n"
                        "9. History\n"
                        "10. Check Wallet Balance\n"
                        "11. Result\n"
                        "12. Unsubscribe\n"
                        "Please select an option: "
                    )
                    if sel13 == "8":
                        bank = input("Please enter your bank: ")
                        num = input("Please enter your account number: ")
                        if num.isnumeric() and len(num) == 10 and bank.isalpha():
                            print("")
                            opt77 = input(
                                "..........\n"
                                "Please check your bank account details and confirm Account Name: Xavier Woods\n"
                                "1. Accept\n"
                                "2. Reject\n"
                                "Please select an option: "
                            )
                            if opt77 == "1":
                                print("Your bank account has been accepted")
                            elif opt77 == "2":
                                print("Your bank account has been rejected")
                            else:
                                print("Invalid option")
                        else:
                            print("Invalid account details")
                    elif sel13 == "9":
                        print("You have no transaction for today")
                    elif sel13 == "10":
                        print("Wallet Balance")
                        print("1. Cashin Wallet Balance: \u20A60")
                        print("2. Cashout Wallet Balance: \u20A60")
                        print("3. Promo Balance: \u20A60")
                    elif sel13 == "11":
                        print("Unavailable at the moment")
                    elif sel13 == "12":
                        print("")
                        sel14 = input(
                            "..........\n"
                            "1. Economy Pack\n"
                            "2. Premium Pack\n"
                            "Please select an option: "
                        )
                        if sel14 == "1":
                            print("")
                            sel15 = input(
                                "..........\n"
                                "For Economy Pack\n"
                                "1. Auto Renewal Daily\n"
                                "2. One-time\n"
                                "Please select an option: "
                            )
                            if sel15 == "1":
                                print("You have successfully unsubscribed from this product")
                            elif sel15 == "2":
                                print("You have successfully unsubscribed from this product")
                            else:
                                print("Invalid option")
                        elif sel14 == "2":
                            print("")
                            sel16 = input(
                                "..........\n"
                                "For Premium Pack\n"
                                "1. Auto Renewal Daily\n"
                                "2. One-time\n"
                                "Please select an option: "
                            )
                            if sel16 == "1":
                                print("You have successfully unsubscribed from this product")
                            elif sel16 == "2":
                                print("You have successfully unsubscribed from this product")
                            else:
                                print("Invalid option")
                        else:
                            print("Invalid option")
                    else:
                        print("Invalid option")
                else:
                    print("Invalid option")
            elif pol24 == "3":
                print("")
                sel17 = input(
                    "..........\n"
                    "PERFECT 10: join to win your share of 5 MILLION Naira\n"
                    "1. Daily auto \u20A650\n"
                    "2. Weekly auto \u20A6100\n" 
                    "3. Daily Onetime \u20A650\n"
                    "4. Weekly Onetime \u20A6100\n"
                    "5. Opt-Out\n"
                    "Please select an option: "
                )
                if sel17 == "1":
                    print("You have successfully subscribed to this product")
                elif sel17 == "2":
                    print("You have successfully subscribed to this product")
                elif sel17 == "3":
                    print("You have successfully subscribed to this product")
                elif sel17 == "4":
                    print("You have successfully subscribed to this product")
                elif sel17 == "5":
                    print("")
                    sel18 = input(
                        "..........\n"
                        "1. Perfect 10 Daily Auto\n"
                        "2. Perfect 10 Daily One-Time\n"
                        "3. Perfect 10 Weekly Auto\n"
                        "4. Perfect 10 Weekly One-Time\n"
                        "Please select an option to opt out: "
                    )
                    if sel18 == "1":
                        print("You have successfully opted out from this product")
                    elif sel18 == "2":
                        print("You have successfully opted out from this product")
                    elif sel18 == "3":
                        print("You have successfully opted out from this product")
                    elif sel18 == "4":
                        print("You have successfully opted out from this product")
                    else:
                        print("Invalid option")
            elif pol24 == "4":
                print("")
                sel19 = input(
                    "..........\n"
                    "1. JOLLY LIFE\n"
                    "2. SPORT BRAIN\n"
                    "3. TREASURE SPIN\n"
                    "4. UNSUBSCRIBE\n"
                    "Please select an option: "
                )
                if sel19 == "1":
                    print("")
                    sel20 = input(
                        "..........\n"
                        "1. Daily Auto @\u20A6100\n"
                        "2. Daily one time @\u20A6100\n"
                        "3. Weekly Auto @\u20A6200\n"
                        "4. Weekly one time @\u20A6200\n"
                        "5. Weekly Auto  @\u20A6500\n"
                        "6. Weekly one time @\u20A6500\n"
                        "Please select an option: "
                    )
                    if sel20 == "1":
                        print("You have successfully subscribed to the product")
                    elif sel20 == "2":
                        print("You have successfully subscribed to the product")
                    elif sel20 == "3":
                        print("You have successfully subscribed to the product")
                    elif sel20 == "4":
                        print("You have successfully subscribed to the product")
                    elif sel20 == "5":
                        print("You have successfully subscribed to the product")
                    elif sel20 == "6":
                        print("You have successfully subscribed to the product")
                    else:
                        print("Invalid option")
                elif sel19 == "2":
                    print("")
                    sel21 = input(
                        "..........\n"
                        "1. Daily Auto @\u20A6100\n"
                        "2. Daily one time @\u20A6100\n"
                        "3. Weekly Auto @\u20A6200\n"
                        "4. Weekly one time @\u20A6200\n"
                        "5. Weekly Auto  @\u20A6500\n"
                        "6. Weekly one time @\u20A6500\n"
                        "Please select an option: "
                    )
                    if sel21 == "1":
                        print("You have successfully subscribed to the product")
                    elif sel21 == "2":
                        print("You have successfully subscribed to the product")
                    elif sel21 == "3":
                        print("You have successfully subscribed to the product")
                    elif sel21 == "4":
                        print("You have successfully subscribed to the product")
                    elif sel21 == "5":
                        print("You have successfully subscribed to the product")
                    elif sel21 == "6":
                        print("You have successfully subscribed to the product")
                    else:
                        print("Invalid option")
                elif sel19 == "3":
                    print("")
                    sel22 = input(
                        "..........\n"
                        "1. Daily Auto @\u20A6100\n"
                        "2. Daily one time @\u20A6100\n"
                        "3. Weekly Auto @\u20A6200\n"
                        "4. Weekly one time @\u20A6200\n"
                        "5. Weekly Auto  @\u20A6500\n"
                        "6. Weekly one time @\u20A6500\n"
                        "Please select an option: "
                    )
                    if sel22 == "1":
                        print("You have successfully subscribed to the product")
                    elif sel22 == "2":
                        print("You have successfully subscribed to the product")
                    elif sel22 == "3":
                        print("You have successfully subscribed to the product")
                    elif sel22 == "4":
                        print("You have successfully subscribed to the product")
                    elif sel22 == "5":
                        print("You have successfully subscribed to the product")
                    elif sel22 == "6":
                        print("You have successfully subscribed to the product")
                    else:
                        print("Invalid option")
                elif sel19 == "4":
                    print("")
                    sel23 = input(
                        "..........\n"
                        "1. JOLLY LIFE\n"
                        "2. SPORT BRAIN\n"
                        "3. TREASURE SPIN\n"
                        "Please select an option: "
                    )
                    if sel23 == "1":
                        print("")
                        sel24 = input(
                            "..........\n"
                            "1. Daily Auto @\u20A6100\n"
                            "2. Daily one time @\u20A6100\n"
                            "3. Weekly Auto @\u20A6200\n"
                            "4. Weekly one time @\u20A6200\n"
                            "5. Weekly Auto  @\u20A6500\n"
                            "6. Weekly one time @\u20A6500\n"
                            "Please select an option: "
                        )
                        if sel24 == "1":
                            print("You have successfully unsubscribed from this product")
                        elif sel24 == "2":
                            print("You have successfully unsubscribed from this product")
                        elif sel24 == "3":
                            print("You have successfully unsubscribed from this product")
                        elif sel24 == "4":
                            print("You have successfully unsubscribed from this product")
                        elif sel24 == "5":
                            print("You have successfully unsubscribed from this product")
                        elif sel24 == "6":
                            print("You have successfully unsubscribed from this product")
                        else:
                            print("Invalid option")
                    elif sel23 == "2":
                        print("")
                        sel25 = input(
                            "..........\n"
                            "1. Daily Auto @\u20A6100\n"
                            "2. Daily one time @\u20A6100\n"
                            "3. Weekly Auto @\u20A6200\n"
                            "4. Weekly one time @\u20A6200\n"
                            "5. Weekly Auto  @\u20A6500\n"
                            "6. Weekly one time @\u20A6500\n"
                            "Please select an option: "
                        )
                        if sel25 == "1":
                            print("You have successfully unsubscribed from this product")
                        elif sel25 == "2":
                            print("You have successfully unsubscribed from this product")
                        elif sel25 == "3":
                            print("You have successfully unsubscribed from this product")
                        elif sel25 == "4":
                            print("You have successfully unsubscribed from this product")
                        elif sel25 == "5":
                            print("You have successfully unsubscribed from this product")
                        elif sel25 == "6":
                            print("You have successfully unsubscribed from this product")
                        else:
                            print("Invalid option")
                    elif sel23 == "3":
                        print("")
                        sel26 = input(
                            "..........\n"
                            "1. Daily Auto @\u20A6100\n"
                            "2. Daily one time @\u20A6100\n"
                            "3. Weekly Auto @\u20A6200\n"
                            "4. Weekly one time @\u20A6200\n"
                            "5. Weekly Auto  @\u20A6500\n"
                            "6. Weekly one time @\u20A6500\n"
                            "Please select an option: "
                        )
                        if sel26 == "1":
                            print("You have successfully unsubscribed from this product")
                        elif sel26 == "2":
                            print("You have successfully unsubscribed from this product")
                        elif sel26 == "3":
                            print("You have successfully unsubscribed from this product")
                        elif sel26 == "4":
                            print("You have successfully unsubscribed from this product")
                        elif sel26 == "5":
                            print("You have successfully unsubscribed from this product")
                        elif sel26 == "6":
                            print("You have successfully unsubscribed from this product")
                        else:
                            print("Invalid option")
                    else:
                        print("Invalid option")
                else:
                    print("Invalid option")
            elif pol24 == "5":
                print("")
                sel27 = input(
                    "..........\n"
                    "Welcome to Africa Winner Service\n"
                    "1. Daily Pack @\u20A6100\n"
                    "2. 3 Days Pack @\u20A6100\n"
                    "3. Weekly @\u20A6200\n"
                    "4. Monthly Pack @\u20A6500\n"
                    "5. Unsubscribe\n"
                    "Please select an option: "
                )
                if sel27 == "1":
                    print("You have successfully subscribed to the product")
                elif sel27 == "2":
                    print("You have successfully subscribed to the product")
                elif sel27 == "3":
                    print("You have successfully subscribed to the product")
                elif sel27 == "4":
                    print("You have successfully subscribed to the product")
                elif sel27 == "5":
                    print("")
                    sel28 = input(
                        "..........\n"
                        "1. Daily Pack\n"
                        "2. 3 Days Pack\n"
                        "3. Weekly\n"
                        "4. Monthly Pack\n"
                        "Please select an option: "
                    )
                    if sel28 == "1":
                        print("")
                        sel29 = input(
                            "..........\n"
                            "1. Auto Renewal Daily\n"
                            "2. One-time\n"
                            "Please select an option: "
                        )
                        if sel29 == "1":
                            print("You have successfully unsubscribed from this product")
                        elif sel29 == "2":
                            print("You have successfully unsubscribed from this product")
                        else:
                            print("Invalid option")
                    elif sel28 == "2":
                        print("")
                        sel30 = input(
                            "..........\n"
                            "1. Auto Renewal Daily\n"
                            "2. One-time\n"
                            "Please select an option: "
                        )
                        if sel30 == "1":
                            print("You have successfully unsubscribed from this product")
                        elif sel30 == "2":
                            print("You have successfully unsubscribed from this product")
                        else:
                            print("Invalid option")
                    elif sel28 == "3":
                        print("")
                        sel31 = input(
                            "..........\n"
                            "1. Auto Renewal Daily\n"
                            "2. One-time\n"
                            "Please select an option: "
                        )
                        if sel31 == "1":
                            print("You have successfully unsubscribed from this product")
                        elif sel31 == "2":
                            print("You have successfully unsubscribed from this product")
                        else:
                            print("Invalid option")
                    elif sel28 == "4":
                        print("")
                        sel32 = input(
                            "..........\n"
                            "1. Auto Renewal Daily\n"
                            "2. One-time\n"
                            "Please select an option: "
                        )
                        if sel32 == "1":
                            print("You have successfully unsubscribed from this product")
                        elif sel32 == "2":
                            print("You have successfully unsubscribed from this product")
                        else:
                            print("Invalid option")
                    else:
                        print("Invalid option")
                else:
                    print("Invalid option")
            elif pol24 == "6":
                print("")
                sel33 = input(
                    "..........\n"
                    "Welcome to ZOOM Lottery\n"
                    "1. Music\n"
                    "2. Dance\n"
                    "3. Sport\n"
                    "4. Business\n"
                    "5. Raider\n"
                    "6. Opt-out\n"
                    "Please select a category: "
                )
                if sel33 == "1":
                    print("")
                    sel34 = input(
                        "..........\n"
                        "1. Daily Auto @\u20A650\n"
                        "2. Weekly Auto @\u20A6100\n"
                        "3. Monthly Auto @\u20A6500\n"
                        "4. Daily one time @\u20A650\n"
                        "5. Weekly one time @\u20A6100\n"
                        "6. Monthly one time @\u20A6500\n"
                        "Please select an option: "
                    )
                    if sel34 == "1":
                        print("You have successfully unsubscribed from this product")
                    elif sel34 == "2":
                        print("You have successfully unsubscribed from this product")
                    elif sel34 == "3":
                        print("You have successfully unsubscribed from this product")
                    elif sel34 == "4":
                        print("You have successfully unsubscribed from this product")
                    elif sel34 == "5":
                        print("You have successfully unsubscribed from this product")
                    elif sel34 == "6":
                        print("You have successfully unsubscribed from this product")
                    else:
                        print("Invalid option")
                elif sel33 == "2":
                    print("")
                    sel35 = input(
                        "..........\n"
                        "1. Daily Auto @\u20A650\n"
                        "2. Weekly Auto @\u20A6100\n"
                        "3. Monthly Auto @\u20A6500\n"
                        "4. Daily one time @\u20A650\n"
                        "5. Weekly one time @\u20A6100\n"
                        "6. Monthly one time @\u20A6500\n"
                        "Please select an option: "
                    )
                    if sel35 == "1":
                        print("You have successfully unsubscribed from this product")
                    elif sel35 == "2":
                        print("You have successfully unsubscribed from this product")
                    elif sel35 == "3":
                        print("You have successfully unsubscribed from this product")
                    elif sel35 == "4":
                        print("You have successfully unsubscribed from this product")
                    elif sel35 == "5":
                        print("You have successfully unsubscribed from this product")
                    elif sel35 == "6":
                        print("You have successfully unsubscribed from this product")
                    else:
                        print("Invalid option")
                elif sel33 == "3":
                    print("")
                    sel36 = input(
                        "..........\n"
                        "1. Daily Auto @\u20A650\n"
                        "2. Weekly Auto @\u20A6100\n"
                        "3. Monthly Auto @\u20A6500\n"
                        "4. Daily one time @\u20A650\n"
                        "5. Weekly one time @\u20A6100\n"
                        "6. Monthly one time @\u20A6500\n"
                        "Please select an option: "
                    )
                    if sel36 == "1":
                        print("You have successfully unsubscribed from this product")
                    elif sel36 == "2":
                        print("You have successfully unsubscribed from this product")
                    elif sel36 == "3":
                        print("You have successfully unsubscribed from this product")
                    elif sel36 == "4":
                        print("You have successfully unsubscribed from this product")
                    elif sel36 == "5":
                        print("You have successfully unsubscribed from this product")
                    elif sel36 == "6":
                        print("You have successfully unsubscribed from this product")
                    else:
                        print("Invalid option")
                elif sel33 == "4":
                    print("")
                    sel37 = input(
                        "..........\n"
                        "1. Daily Auto @\u20A650\n"
                        "2. Weekly Auto @\u20A6100\n"
                        "3. Monthly Auto @\u20A6500\n"
                        "4. Daily one time @\u20A650\n"
                        "5. Weekly one time @\u20A6100\n"
                        "6. Monthly one time @\u20A6500\n"
                        "Please select an option: "
                    )
                    if sel37 == "1":
                        print("You have successfully unsubscribed from this product")
                    elif sel37 == "2":
                        print("You have successfully unsubscribed from this product")
                    elif sel37 == "3":
                        print("You have successfully unsubscribed from this product")
                    elif sel37 == "4":
                        print("You have successfully unsubscribed from this product")
                    elif sel37 == "5":
                        print("You have successfully unsubscribed from this product")
                    elif sel37 == "6":
                        print("You have successfully unsubscribed from this product")
                    else:
                        print("Invalid option")
                elif sel33 == "5":
                    print("")
                    sel38 = input(
                        "..........\n"
                        "1. Weekly Auto @\u20A6100\n"
                        "2. Weekly one time @\u20A6100\n"
                        "Please select an option: "
                    )
                    if sel38 == "1":
                        print("You have successfully unsubscribed from this product")
                    elif sel38 == "2":
                        print("You have successfully unsubscribed from this product")
                    else:
                        print("Invalid option")
                elif sel33 == "6":
                    print("")
                    sel39 = input(
                        "..........\n"
                        "1. Music\n"
                        "2. Dance\n"
                        "3. Sport\n"
                        "4. Business\n"
                        "5. Raider\n"
                        "Please select an option to opt out: "
                    )
                    if sel39 == "1":
                        print("")
                        sel37 = input(
                            "..........\n"
                            "1. Daily Auto @\u20A650\n"
                            "2. Weekly Auto @\u20A6100\n"
                            "3. Monthly Auto @\u20A6500\n"
                            "4. Daily one time @\u20A650\n"
                            "5. Weekly one time @\u20A6100\n"
                            "88. Next\n"
                            "Please select an option: "
                        )
                        if sel37 == "1":
                            print("You have successfully opted out from this product")
                        elif sel37 == "2":
                            print("You have successfully opted out from this product")
                        elif sel37 == "3":
                            print("You have successfully opted out from this product")
                        elif sel37 == "4":
                            print("You have successfully opted out from this product")
                        elif sel37 == "5":
                            print("You have successfully opted out from this product")
                        elif sel37 == "88":
                            print("")
                            sel38 = input(
                                "..........\n"
                                "6. Monthly one time @\u20A6500\n"
                                "Please select an option: "
                            )
                            if sel38 == "6":
                                print("You have successfully opted out from this product")
                            else:
                                print("Invalid option")
                        else:
                            print("Invalid option")
                    elif sel39 == "2":
                        print("")
                        sel37 = input(
                            "..........\n"
                            "1. Daily Auto @\u20A650\n"
                            "2. Weekly Auto @\u20A6100\n"
                            "3. Monthly Auto @\u20A6500\n"
                            "4. Daily one time @\u20A650\n"
                            "5. Weekly one time @\u20A6100\n"
                            "88. Next\n"
                            "Please select an option: "
                        )
                        if sel37 == "1":
                            print("You have successfully opted out from this product")
                        elif sel37 == "2":
                            print("You have successfully opted out from this product")
                        elif sel37 == "3":
                            print("You have successfully opted out from this product")
                        elif sel37 == "4":
                            print("You have successfully opted out from this product")
                        elif sel37 == "5":
                            print("You have successfully opted out from this product")
                        elif sel37 == "88":
                            print("")
                            sel38 = input(
                                "..........\n"
                                "6. Monthly one time @\u20A6500\n"
                                "Please select an option: "
                            )
                            if sel38 == "6":
                                print("You have successfully opted out from this product")
                            else:
                                print("Invalid option")
                        else:
                            print("Invalid option")
                    elif sel39 == "3":
                        print("")
                        sel37 = input(
                            "..........\n"
                            "1. Daily Auto @\u20A650\n"
                            "2. Weekly Auto @\u20A6100\n"
                            "3. Monthly Auto @\u20A6500\n"
                            "4. Daily one time @\u20A650\n"
                            "5. Weekly one time @\u20A6100\n"
                            "88. Next\n"
                            "Please select an option: "
                        )
                        if sel37 == "1":
                            print("You have successfully opted out from this product")
                        elif sel37 == "2":
                            print("You have successfully opted out from this product")
                        elif sel37 == "3":
                            print("You have successfully opted out from this product")
                        elif sel37 == "4":
                            print("You have successfully opted out from this product")
                        elif sel37 == "5":
                            print("You have successfully opted out from this product")
                        elif sel37 == "88":
                            print("")
                            sel38 = input(
                                "..........\n"
                                "6. Monthly one time @\u20A6500\n"
                                "Please select an option: "
                            )
                            if sel38 == "6":
                                print("You have successfully opted out from this product")
                            else:
                                print("Invalid option")
                        else:
                            print("Invalid option")
                    elif sel39 == "4":
                        print("")
                        sel37 = input(
                            "..........\n"
                            "1. Daily Auto @\u20A650\n"
                            "2. Weekly Auto @\u20A6100\n"
                            "3. Monthly Auto @\u20A6500\n"
                            "4. Daily one time @\u20A650\n"
                            "5. Weekly one time @\u20A6100\n"
                            "88. Next\n"
                            "Please select an option: "
                        )
                        if sel37 == "1":
                            print("You have successfully opted out from this product")
                        elif sel37 == "2":
                            print("You have successfully opted out from this product")
                        elif sel37 == "3":
                            print("You have successfully opted out from this product")
                        elif sel37 == "4":
                            print("You have successfully opted out from this product")
                        elif sel37 == "5":
                            print("You have successfully opted out from this product")
                        elif sel37 == "88":
                            print("")
                            sel38 = input(
                                "..........\n"
                                "6. Monthly one time @\u20A6500\n"
                                "Please select an option: "
                            )
                            if sel38 == "6":
                                print("You have successfully opted out from this product")
                            else:
                                print("Invalid option")
                        else:
                            print("Invalid option")
                    elif sel39 == "5":
                        print("")
                        sel37 = input(
                            "..........\n"
                            "1. Weekly Auto @\u20A6100\n"
                            "2. Weekly one time @\u20A6100\n"
                            "Please select an option: "
                        )
                        if sel37 == "1":
                            print("You have successfully opted out from this product")
                        elif sel37 == "2":
                            print("You have successfully opted out from this product")
                        else:
                            print("Invalid option")
                    else:
                        print("Invalid option")
                else:
                    print("Invalid option")
            else:
                print("Invalid option")
        elif pol == "4":
            print("")
            sel40 = input(
                "..........\n"
                "1. Glo Magazine\n"
                "2. TAPESTRY COMEDY\n"
                "Please select an option: "
            )
            if sel40 == "1":
                print("")
                sel25 = input(
                    "..........\n"
                    "Welcome to Glo Magazine Service\n"
                    "1. Daily Auto @\u20A630\n"
                    "2. Weekly Auto @\u20A6100\n"
                    "3. Monthly Auto @\u20A6200\n"
                    "4. Daily one time @\u20A630\n"
                    "5. Weekly one time @\u20A6100\n"
                    "6. Monthly one time @\u20A6200\n"
                    "Please select an option: "
                )
                if sel25 == "1":
                    print("You have successfully subscribed from this product")
                elif sel25 == "2":
                    print("You have successfully subscribed from this product")
                elif sel25 == "3":
                    print("You have successfully subscribed from this product")
                elif sel25 == "4":
                    print("You have successfully subscribed from this product")
                elif sel25 == "5":
                    print("You have successfully subscribed from this product")
                elif sel25 == "6":
                    print("You have successfully subscribed from this product")
                else:
                    print("Invalid option")
            elif sel40 == "2":
                print("")
                sel99 = input(
                    "..........\n"
                    "1. TAPESTRY COMEDY\n"
                    "2. MDUNDO MUSIC\n"
                    "3. UNSUBSCRIBE\n"
                    "Please select an option: "
                )
                if sel99 == "1":
                    print("")
                    sel25 = input(
                        "..........\n"
                        "1. Daily Auto @\u20A6100\n"
                        "2. Weekly Auto @\u20A6200\n"
                        "3. Daily one time @\u20A6100\n"
                        "4. Weekly one time @\u20A6200\n"
                        "Please select an option: "
                    )
                    if sel25 == "1":
                        print("You have successfully subscribed from this product")
                    elif sel25 == "2":
                        print("You have successfully subscribed from this product")
                    elif sel25 == "3":
                        print("You have successfully subscribed from this product")
                    elif sel25 == "4":
                        print("You have successfully subscribed from this product")
                    else:
                        print("Invalid option")
                elif sel99 == "2":
                    print("")
                    sel25 = input(
                        "..........\n"
                        "1. Daily Auto @\u20A6100\n"
                        "2. Weekly Auto @\u20A6300\n"
                        "3. Daily one time @\u20A6100\n"
                        "4. Weekly one time @\u20A6300\n"
                        "Please select an option: "
                    )
                    if sel25 == "1":
                        print("You have successfully subscribed from this product")
                    elif sel25 == "2":
                        print("You have successfully subscribed from this product")
                    elif sel25 == "3":
                        print("You have successfully subscribed from this product")
                    elif sel25 == "4":
                        print("You have successfully subscribed from this product")
                    else:
                        print("Invalid option")
                elif sel99 == "3":
                    print("")
                    sel89 = input(
                        "..........\n"
                        "1. TAPESTRY\n"
                        "2. MDUNDO\n"
                        "Please select an option"
                    )
                    if sel89 == "1":
                        print("")
                        sel25 = input(
                            "..........\n"
                            "1. Daily Auto\n"
                            "2. Weekly Auto\n"
                            "3. Daily one time\n"
                            "4. Weekly one time\n"
                            "Please select an option: "
                        )
                        if sel25 == "1":
                            print("You have successfully unsubscribed from this product")
                        elif sel25 == "2":
                            print("You have successfully unsubscribed from this product")
                        elif sel25 == "3":
                            print("You have successfully unsubscribed from this product")
                        elif sel25 == "4":
                            print("You have successfully unsubscribed from this product")
                        else:
                            print("Invalid option")
                    elif sel89 == "2":
                        print("")
                        sel25 = input(
                            "..........\n"
                            "1. Daily Auto\n"
                            "2. Weekly Auto\n"
                            "3. Daily one time\n"
                            "4. Weekly one time\n"
                            "Please select an option: "
                        )
                        if sel25 == "1":
                            print("You have successfully unsubscribed from this product")
                        elif sel25 == "2":
                            print("You have successfully unsubscribed from this product")
                        elif sel25 == "3":
                            print("You have successfully unsubscribed from this product")
                        elif sel25 == "4":
                            print("You have successfully unsubscribed from this product")
                        else:
                            print("Invalid option")
                    else:
                        print("Invalid option")
                else:
                    print("Invalid option")
            else:
                print("Invalid option")
        elif pol == "5":
            print("")
            sel41 = input(
                "..........\n"
                "1. Sports Video Portal\n"
                "2. Sports Portal\n"
                "Please select an option: "
            )
            if sel41 == "1":
                print("")
                sel37 = input(
                    "..........\n"
                    "Welcome to Sports Video Portal Service"
                    "1. Daily Auto @\u20A630\n"
                    "2. Weekly Auto @\u20A6100\n"
                    "3. Monthly Auto @\u20A6200\n"
                    "4. Daily one time @\u20A630\n"
                    "5. Weekly one time @\u20A6100\n"
                    "88. Next\n"
                    "Please select an option: "
                )
                if sel37 == "1":
                    print("You have successfully subscribed to this product")
                elif sel37 == "2":
                    print("You have successfully subscribed to this this product")
                elif sel37 == "3":
                    print("You have successfully subscribed to this this product")
                elif sel37 == "4":
                    print("You have successfully subscribed to this this product")
                elif sel37 == "5":
                    print("You have successfully subscribed to this this product")
                elif sel37 == "88":
                    print("")
                    sel38 = input(
                        "..........\n"
                        "6. Monthly one time @\u20A6200\n"
                        "Please select an option: "
                    )
                    if sel38 == "6":
                        print("You have successfully subscribed to this this product")
                    else:
                        print("Invalid option")
                else:
                    print("Invalid option")
            elif sel41 == "2":
                print("")
                sel38 = input(
                    "..........\n"
                    "Welcome to Sports Portal Service"
                    "1. Daily Auto @\u20A620\n"
                    "2. Weekly Auto @\u20A660\n"
                    "3. Monthly Auto @\u20A6150\n"
                    "4. Daily one time @\u20A620\n"
                    "5. Weekly one time @\u20A660\n"
                    "6. Monthly one time @\u20A6150\n"
                    "Please select an option: "
                )
                if sel38 == "1":
                    print("You have successfully subscribed to this product")
                elif sel38 == "2":
                    print("You have successfully subscribed to this this product")
                elif sel38 == "3":
                    print("You have successfully subscribed to this this product")
                elif sel38 == "4":
                    print("You have successfully subscribed to this this product")
                elif sel38 == "5":
                    print("You have successfully subscribed to this this product")
                elif sel38 == "6":
                        print("You have successfully subscribed to this this product")
                else:
                    print("Invalid option")
            else:
                print("Invalid option")
        elif pol == "6":
            print("This service is not available. Please try again later")
        elif pol == "7":
            print("")
            sel15 = input(
                "..........\n"
                "Dear Customer, Welcome, you are eligible for \u20A650. Reply with\n"
                "1. My BMC Account\n"
                "2. Borrow Credit\n"
                "3. Borrow Data\n"
                "4. Borrow Credit for Others\n"
                "5. Borrow Data for Others\n"
                "Please select an option: "
            )
            if sel15 == "1":
                print("")
                sel16 = input(
                    "..........\n"
                    "1. Balance\n"
                    "2. Payment\n"
                    "3. Repay Loan\n"
                    "Please select an option: "
                )
                if sel16 == "1":
                    print("You have no advance airtime uncleared balance")
                elif sel16 == "2":
                    print("Connection problem or invalid MMI code")
                elif sel16 == "3":
                    print("Dear Customer, your repayment request is being processed")
                else:
                    print("Invalid option")
            elif sel15 == "2":
                print("")
                sel17 = input(
                    "..........\n"
                    "1. \u20A650\n"
                    "2. \u20A625\n"
                    "3. Help\n"
                    "4. Balance\n"
                    "Please select an option: "
                )
                if sel17 == "1":
                    print("You have successfully borrowed \u20A650")
                elif sel17 == "2":
                    print("You have successfully borrowed \u20A625")
                elif sel17 == "3":
                    print("Connection problem or invalid MMI code")
                elif sel17 == "4":
                    print("You have no advance airtime uncleared balance")
                else:
                    print("Invalid option")
            elif sel15 == "3":
                print("")
                sel18 = input(
                    "..........\n"
                    "You are eligible for \u20A650\n"
                    "1. \u20A650 = 40MB + 5MB\n"
                    "Please select an option:"
                )
                if sel18 == "1":
                    print("You have successfully borrowed 40MB + 5MB at \u20A650")
                else:
                    print("Invalid option")
            elif sel15 == "4":
                print("")
                sel19 = input(
                    "..........\n"
                    "1. \u20A650\n"
                    "2. \u20A625\n"
                    "3. Help\n"
                    "4. Balance\n"
                    "Please select an option: "
                )
                tel = input("Enter phone number of the recipient: ")
                if sel19 == "1":
                    if len(tel) == 11 and tel.isnumeric() and (tel.startswith("070") or tel.startswith("080") or tel.startswith("081") or tel.startswith("090") or tel.startswith("091")):
                        print(f"You have successfully credited {tel} with \u20A650")
                    else:
                        print("Invalid phone number")
                elif sel19 == "2":
                    if len(tel) == 11 and tel.isnumeric() and (tel.startswith("070") or tel.startswith("080") or tel.startswith("081") or tel.startswith("090") or tel.startswith("091")):
                        print(f"You have successfully credited {tel} with \u20A625")
                    else:
                        print("Invalid phone number")
                elif sel19 == "3":
                    print("Connection problem or invalid MMI code")
                elif sel19 == "4":
                    print("You have no advance airtime uncleared balance")
                else:
                    print("Invalid option")
            elif sel15 == "5":
                print("")
                sel20 = input(
                    "..........\n"
                    "You are eligible for \u20A650\n"
                    "1. \u20A650 = 40MB + 5MB\n"
                    "Please select an option:"
                )
                tel1 = input("Enter phone number of the recipient: ")
                if sel20 == "1":
                    if len(tel1) == 11 and tel1.isnumeric() and (tel1.startswith("070") or tel1.startswith("080") or tel1.startswith("081") or tel1.startswith("090") or tel1.startswith("091")):
                        print(f"You have successfully credited {tel1} with 40MB + 5MB at \u20A650")
                    else:
                        print("Invalid phone number")
            else:
                print("Invalid option")
        elif pol == "8":
            print("Glo Cloud Service. 1st Month Free")
            print("Please visit https://glocloud.gloworld.com to subscribe")
        elif pol == "9":
            print("")
            opt = input(
                "..........\n"
                "1. Gaming Service\n"
                "2. Educational service\n"
                "3. Lottery Service\n"
                "4. Entertainment\n" 
                "5. Sports Service\n" 
                "6. Caller Tunes Service\n"
                "7. Glo Cloud Service\n"
                "Please select an option to unsubscribe: "
            )
            if opt == "1":
                print("")
                pol1 = input(
                    "..........\n"
                    "1. Gaming Portal\n"
                    "2. Gaming Tournament\n"
                    "3. Edu games\n"
                    "4. Game Box\n"
                    "5. Games Play\n"
                    "6. Glo Games Club\n"
                    "7. Glo Kidjo TV\n"
                    "8. Wazoo Play\n"
                    "Please select an option: "
                )
                if pol1 == "1":
                    print("")
                    pol2 = input(
                        "..........\n"
                        "1. Daily Auto\n"
                        "Please select the Gaming Portal pack to Unsubscribe:"
                    )
                    if pol2 == "1":
                        print("You have successfully unsubscribed")
                    else:
                        print("Invalid option")
                elif pol1 == "2":
                    print("")
                    pol2 = input(
                        "..........\n"
                        "1. Daily Auto\n"
                        "2. Weekly Auto\n"
                        "3. Monthly Auto\n"
                        "Please select the Gaming tournament pack to Unsubscribe:"
                    )
                    if pol2 == "1":
                        print("You have successfully unsubscribed")
                    elif pol2 == "2":
                        print("You have successfully unsubscribed")
                    elif pol2 == "3":
                        print("You have successfully unsubscribed")
                    else:
                        print("Invalid option")
                elif pol1 == "3":
                    print("")
                    pol2 = input(
                        "..........\n"
                        "1. Daily Auto\n"
                        "2. Weekly Auto\n"
                        "3. Monthly Auto\n"
                        "Please select the Edu games pack to Unsubscribe:"
                    )
                    if pol2 == "1":
                        print("You have successfully unsubscribed")
                    elif pol2 == "2":
                        print("You have successfully unsubscribed")
                    elif pol2 == "3":
                        print("You have successfully unsubscribed")
                    else:
                        print("Invalid option")
                elif pol1 == "4":
                    print("")
                    pol2 = input(
                        "..........\n"
                        "1. Daily Auto\n"
                        "2. Weekly Auto\n"
                        "3. Monthly Auto\n"
                        "Please select the Glo gamebox pack to Unsubscribe:"
                    )
                    if pol2 == "1":
                        print("You have successfully unsubscribed")
                    elif pol2 == "2":
                        print("You have successfully unsubscribed")
                    elif pol2 == "3":
                        print("You have successfully unsubscribed")
                    else:
                        print("Invalid option")
                elif pol1 == "5":
                    print("")
                    pol2 = input(
                        "..........\n"
                        "1. Daily Auto\n"
                        "2. Weekly Auto\n"
                        "3. Monthly Auto\n"
                        "Please select the Glo gamebox pack to Unsubscribe:"
                    )
                    if pol2 == "1":
                        print("You have successfully unsubscribed")
                    elif pol2 == "2":
                        print("You have successfully unsubscribed")
                    elif pol2 == "3":
                        print("You have successfully unsubscribed")
                    else:
                        print("Invalid option")
                elif pol1 == "6":
                    print("")
                    pol2 = input(
                        "..........\n"
                        "1. Daily pack\n"
                        "2. Weekly pack\n"
                        "3. Monthly pack\n"
                        "Please select the pack to unsubscribe:"
                    )
                    if pol2 == "1":
                        print("You have successfully unsubscribed")
                    elif pol2 == "2":
                        print("You have successfully unsubscribed")
                    elif pol2 == "3":
                        print("You have successfully unsubscribed")
                    else:
                        print("Invalid option")
                elif pol1 == "7":
                    print("You have successfully unsubscribed to the plan")
                elif pol1 == "8":
                    print("You have successfully subscribed to the product")
                else:
                    print("Invalid option")
            elif opt == "2":
                print("")
                pol2 = input(
                    "..........\n"
                    "1. Language Learning - Busuu\n"
                    "2. Edu Video\n"
                    "Please select the pack you wish to unsubscribe: "
                )
                if pol2 == "1":
                    print("")
                    pol3 = input(
                        "..........\n"
                        "1. Daily Auto\n"
                        "2. Weekly Auto\n"
                        "Please select the busuu pack to unsubscribe:"
                    )
                    if pol2 == "1":
                        print("You have successfully unsubscribed")
                    elif pol2 == "2":
                        print("You have successfully unsubscribed")
                    else:
                        print("Invalid option")
                elif pol2 == "2":
                    print("")
                    pol3 = input(
                        "..........\n"
                        "1. Daily Auto\n"
                        "2. Weekly Auto\n"
                        "3. Monthly Auto\n"
                        "Please select the edu video pack to Unsubscribe:"
                    )
                    if pol2 == "1":
                        print("You have successfully unsubscribed")
                    elif pol2 == "2":
                        print("You have successfully unsubscribed")
                    elif pol2 == "3":
                        print("You have successfully unsubscribed")
                    else:
                        print("Invalid option")
                else:
                    print("Invalid option")
            elif opt == "3":
                print("")
                pol24 = input(
                    "..........\n"
                    "1. Green Lotto\n"
                    "2. Lucky Number\n"
                    "3. Perfect 10\n"
                    "4. Jolly Suite\n"
                    "5. Africa Winner\n"
                    "6. Zoom Lottery\n"
                    "Please select an option: "
                )
                if pol24 == "1":
                    print("")
                    sel14 = input(
                        "..........\n"
                        "1. Economy Pack\n"
                        "2. Premium Pack\n"
                        "Please select an option: "
                    )
                    if sel14 == "1":
                        print("")
                        sel15 = input(
                            "..........\n"
                            "For Economy Pack\n"
                            "1. Auto Renewal Daily\n"
                            "2. One-time\n"
                            "Please select an option: "
                        )
                        if sel15 == "1":
                            print("You have successfully unsubscribed from this product")
                        elif sel15 == "2":
                            print("You have successfully unsubscribed from this product")
                        else:
                            print("Invalid option")
                    elif sel14 == "2":
                        print("")
                        sel16 = input(
                            "..........\n"
                            "For Premium Pack\n"
                            "1. Auto Renewal Daily\n"
                            "2. One-time\n"
                            "Please select an option: "
                        )
                        if sel16 == "1":
                            print("You have successfully unsubscribed from this product")
                        elif sel16 == "2":
                            print("You have successfully unsubscribed from this product")
                        else:
                            print("Invalid option")
                    else:
                        print("Invalid option")
                elif pol24 == "2":
                    print("")
                    sel5 = input(
                        "..........\n"
                        "1. Lucky number Economy\n"
                        "2. Lucky number Max\n"
                        "3. Lucky number Premium\n"
                        "Please select a package: "
                    )
                    if sel5 == "1":
                        print("")
                        sel6 = input(
                            "..........\n"
                            "1. Lucky Number Economy Auto\n"
                            "2. Lucky Number Economy one time\n"
                            "Please select an option"
                        )
                        if sel6 == "1":
                            print("You have successfully unsubscribed from lucky number economy")
                        elif sel6 == "2":
                            print("You have successfully unsubscribed from lucky number economy")
                        else:
                            print("Invalid option")
                    elif sel5 == "2":
                        print("")
                        sel7 = input(
                            "..........\n"
                            "1. Lucky Number Max Auto\n"
                            "2. Lucky Number Max one time\n"
                            "Please select an option"
                        )
                        if sel7 == "1":
                            print("You have successfully unsubscribed from lucky number max")
                        elif sel7 == "2":
                            print("You have successfully unsubscribed from lucky number max")
                        else:
                            print("Invalid option")
                    elif sel5 == "3":
                        print("")
                        sel8 = input(
                            "..........\n"
                            "1. Lucky Number Premium Auto\n"
                            "2. Lucky Number Premium one time\n"
                            "Please select an option"
                        )
                        if sel8 == "1":
                            print("You have successfully unsubscribed from lucky number premium")
                        elif sel8 == "2":
                            print("You have successfully unsubscribed from lucky number premium")
                        else:
                            print("Invalid option")
                    else:
                        print("Invalid option")
                elif pol24 == "3":
                    print("You have successfully unsubscribed")
                elif pol24 == "4":
                    sel23 = input(
                    "1. JOLLY LIFE\n"
                    "2. SPORT BRAIN\n"
                    "3. TREASURE SPIN\n"
                    "Please select an option: "
                    )
                    if sel23 == "1":
                        print("")
                        sel24 = input(
                            "..........\n"
                            "1. Daily Auto @\u20A6100\n"
                            "2. Daily one time @\u20A6100\n"
                            "3. Weekly Auto @\u20A6200\n"
                            "4. Weekly one time @\u20A6200\n"
                            "5. Weekly Auto  @\u20A6500\n"
                            "6. Weekly one time @\u20A6500\n"
                            "Please select an option: "
                        )
                        if sel24 == "1":
                            print("You have successfully unsubscribed from this product")
                        elif sel24 == "2":
                            print("You have successfully unsubscribed from this product")
                        elif sel24 == "3":
                            print("You have successfully unsubscribed from this product")
                        elif sel24 == "4":
                            print("You have successfully unsubscribed from this product")
                        elif sel24 == "5":
                            print("You have successfully unsubscribed from this product")
                        elif sel24 == "6":
                            print("You have successfully unsubscribed from this product")
                        else:
                            print("Invalid option")
                    elif sel23 == "2":
                        print("")
                        sel25 = input(
                            "..........\n"
                            "1. Daily Auto @\u20A6100\n"
                            "2. Daily one time @\u20A6100\n"
                            "3. Weekly Auto @\u20A6200\n"
                            "4. Weekly one time @\u20A6200\n"
                            "5. Weekly Auto  @\u20A6500\n"
                            "6. Weekly one time @\u20A6500\n"
                            "Please select an option: "
                        )
                        if sel25 == "1":
                            print("You have successfully unsubscribed from this product")
                        elif sel25 == "2":
                            print("You have successfully unsubscribed from this product")
                        elif sel25 == "3":
                            print("You have successfully unsubscribed from this product")
                        elif sel25 == "4":
                            print("You have successfully unsubscribed from this product")
                        elif sel25 == "5":
                            print("You have successfully unsubscribed from this product")
                        elif sel25 == "6":
                            print("You have successfully unsubscribed from this product")
                        else:
                            print("Invalid option")
                    elif sel23 == "3":
                        print("")
                        sel26 = input(
                            "..........\n"
                            "1. Daily Auto @\u20A6100\n"
                            "2. Daily one time @\u20A6100\n"
                            "3. Weekly Auto @\u20A6200\n"
                            "4. Weekly one time @\u20A6200\n"
                            "5. Weekly Auto  @\u20A6500\n"
                            "6. Weekly one time @\u20A6500\n"
                            "Please select an option: "
                        )
                        if sel26 == "1":
                            print("You have successfully unsubscribed from this product")
                        elif sel26 == "2":
                            print("You have successfully unsubscribed from this product")
                        elif sel26 == "3":
                            print("You have successfully unsubscribed from this product")
                        elif sel26 == "4":
                            print("You have successfully unsubscribed from this product")
                        elif sel26 == "5":
                            print("You have successfully unsubscribed from this product")
                        elif sel26 == "6":
                            print("You have successfully unsubscribed from this product")
                        else:
                            print("Invalid option")
                    else:
                        print("Invalid option")
                elif pol24 == "5":
                    print("")
                    sel28 = input(
                        "..........\n"
                        "1. Daily Pack\n"
                        "2. 3 Days Pack\n"
                        "3. Weekly\n"
                        "4. Monthly Pack\n"
                        "Please select an option: "
                    )
                    if sel28 == "1":
                        print("")
                        sel29 = input(
                            "..........\n"
                            "1. Auto Renewal Daily\n"
                            "2. One-time\n"
                            "Please select an option: "
                        )
                        if sel29 == "1":
                            print("You have successfully unsubscribed from this product")
                        elif sel29 == "2":
                            print("You have successfully unsubscribed from this product")
                        else:
                            print("Invalid option")
                    elif sel28 == "2":
                        print("")
                        sel30 = input(
                            "..........\n"
                            "1. Auto Renewal Daily\n"
                            "2. One-time\n"
                            "Please select an option: "
                        )
                        if sel30 == "1":
                            print("You have successfully unsubscribed from this product")
                        elif sel30 == "2":
                            print("You have successfully unsubscribed from this product")
                        else:
                            print("Invalid option")
                    elif sel28 == "3":
                        print("")
                        sel31 = input(
                            "..........\n"
                            "1. Auto Renewal Daily\n"
                            "2. One-time\n"
                            "Please select an option: "
                        )
                        if sel31 == "1":
                            print("You have successfully unsubscribed from this product")
                        elif sel31 == "2":
                            print("You have successfully unsubscribed from this product")
                        else:
                            print("Invalid option")
                    elif sel28 == "4":
                        print("")
                        sel32 = input(
                            "..........\n"
                            "1. Auto Renewal Daily\n"
                            "2. One-time\n"
                            "Please select an option: "
                        )
                        if sel32 == "1":
                            print("You have successfully unsubscribed from this product")
                        elif sel32 == "2":
                            print("You have successfully unsubscribed from this product")
                        else:
                            print("Invalid option")
                    else:
                        print("Invalid option")
                elif pol24 == "6":
                    print("You have successfully unsubscribed from this product")
                else:
                    print("Invalid option")
            elif opt == "4":
                print("You have successfully unsubscribed")
            elif opt == "5":
                print("")
                sel41 = input(
                    "..........\n"
                    "1. Sports Video Portal\n"
                    "2. Sports Portal\n"
                    "Please select an option: "
                )
                if sel41 == "1":
                    print("")
                    sel37 = input(
                        "..........\n"
                        "Welcome to Sports Video Portal Service"
                        "1. Daily Auto\n"
                        "2. Weekly Auto\n"
                        "3. Monthly Auto\n"
                        "Please select an option to unsubscribe from: "
                    )
                    if sel37 == "1":
                        print("You have successfully unsubscribed from this product")
                    elif sel37 == "2":
                        print("You have successfully unsubscribed from this product")
                    elif sel37 == "3":
                        print("You have successfully unsubscribed from this product")
                    else:
                        print("Invalid option")
                elif sel41 == "2":
                    print("")
                    sel38 = input(
                        "..........\n"
                        "Welcome to Sports Portal Service"
                        "1. Daily Auto\n"
                        "2. Weekly Auto\n"
                        "3. Monthly Auto\n"
                        "Please select an option you want to unsubscribe from: "
                    )
                    if sel38 == "1":
                        print("You have successfully unsubscribed from this product")
                    elif sel38 == "2":
                        print("You have successfully unsubscribed from this product")
                    elif sel38 == "3":
                        print("You have successfully unsubscribed from this product")
                    else:
                        print("Invalid option")
                else:
                    print("Invalid option")
            elif opt == "6":
                print("This service is not available. Please try again later")
            elif opt == "7":
                print("Please visit https://glocloud.gloworld.com to unsubscribe")
            else:
                print("Invalid option")
        else:
            print("Invalid option")
    elif options == "8":
        print("")
        sel55 = input(
            "..........\n"
            "Recharge and win assured cashback, exciting prizes and chance to win up to \u20A6100M every week:\n"
            "1. Opt-In\n"
            "2. Opt-Out\n"
            "Please select an option: "
        )
        if sel55 == "1":
            print("Dear Customer, You have successfully opted-in for promo. Keep recharging to win cashback, exciting prizes up to \u20A6100M everyweek")
        elif sel55 == "2":
            print("Dear Customer, You have successfully opted-out for promo. Keep recharging to win cashback, exciting prizes up to \u20A6100M everyweek")
        else:
            print("Invalid option")
    elif options == "9":
        print("")
        sel11 = input(
            "..........\n"
            "Exciting Offers Only On Glo Cafe App\n"
            "1. 100GB Bonus Data\n"
            "2. Recharge Bonus - 100%\n"
            "3. 10% More On Data Plans\n"
            "4. App Only Special Data Bundles\n"
            "5. Glo Cafe App Link\n"
            "Please select an option: "
        )
        if sel11 == "1":
            print("Only For New Users: Download & Register Glo Cafe App & get 100GB Bonus Data.")
            print("Hurry! Download Now! Glo Cafe App download link")
        elif sel11 == "2":
            print("100% Recharge Bonus on Cafe: Get 100% Recharge Bonus On All Recharges")
            print("Done through Glo Cafe App. Download the Glo Cafe App now!")
        elif sel11 == "3":
            print("10% Bonus Data On Data Plans purchased through Glo Cafe App, Example: Get 500MB ]")
            print("more in \u20A62000 Data Bundle on Glo Cafe App. Glo Cafe App download link")
        elif sel11 == "4":
            print("Special Bundles: Available Only On App, \u20A6200 =  1GB 1D, \u20A6300 = 2GB 1D,")
            print("\u20A6500 = 3.5GB 2D, \u20A62000 = 15GB 7D. To enjoy, get the App Now!")
        elif sel11 == "5":
            print("Enjoy Glo Cafe Offers! 100GB Bonus + 100% Recharge Bonus + 10% More Data + Special Data")
            print("Bundles App Download Links: Android:bit.ly/3zQUZRA, iOS:apple.co/3o60s4v")
        else:
            print("Invalid option")
    elif options == "10":
        print("")
        sel2 = input(
            "..........\n"
            "1. My Tariff Plan\n"
            "2. Intl Call Offers\n"
            "3. Data Roaming Offers\n"
            "4. Glo Talk On\n"
            "5. Glo Super Talk\n"
            "6. Always On\n"
            "Please select an option: "
        )
        if sel2 == "1":
            print("")
            sel3 = input(
                "..........\n"
                "1. My Package\n"
                "2. My Number\n"
                "3. Friends and Family Number\n"
                "4. Easy Share\n"
            )
            if sel3 == "1":
                print("")
                sel4 = input(
                    "..........\n"
                    "1. To Know Your Package, Dial #100#\n"
                    "2. To Migrate to other profile, Dial *100#\n"
                )
                if sel4 == "1":
                    print("To Know Your Package, Dial #100#")
                elif sel4 == "2":
                    print("To Migrate to other profile, Dial *100")
                else:
                    print("")
            elif sel3 == "2":
                print("Dear customer, to know your Glo Number, pleas dial *777#")
            elif sel3 == "3":
                print("")
                sel4 = input(
                    "..........\n"
                    "1. To Manage Friends & Family, Dial *606*1#\n"
                    "2. View Friends & Family list, Dial *170*50#\n"
                )
                if sel4 == "1":
                    print("To Manage Friends & Family, Dial *606*1#")
                elif sel4 == "2":
                    print("View Friends & Family list, Dial *170*50#")
                else:
                    print("Invalid option")
            elif sel3 == "4":
                print("Dear customer, for Me2U please dial *131*Phone Number*Amount*PIN#")
            else:
                print("Invalid option")
        elif sel2 == "2":
            print("")
            sel6 = input(
                "..........\n"
                "1. \u20A6100 = 3 Min 1 Day\n"
                "2. \u20A6200 = 7 Min 3 Days\n"
                "3. \u20A6500 = 18 Min 10 Days\n"
                "4. \u20A61000 = 37 Min 30 Days\n"
                "5. List of 8 countries\n"
                "6. Check IDD Pack Balance\n"
                "Please select an option: "
            )
            if sel6 == "1":
                print("You have successfully activated an international call offer, valid for 3 Min for a day")
            elif sel6 == "2":
                print("You have successfully activated an international call offer, valid for 7 Min for 3 days")
            elif sel6 == "3":
                print("You have successfully activated an international call offer, valid for 18 Min for 10 days")
            elif sel6 == "4":
                print("You have successfully activated an international call offer, valid for 3 Min for a day")
            elif sel6 == "5":
                print("USA, Canada, Bangladesh, Malaysia, Puerto Rico, Romania, Norway, Peru")
            elif sel6 == "6":
                print("Dear Customer, you don't have a bundle. Kindly dial *777# to buy a bundle of your choice")
            else:
                print("Invalid option")
        elif sel2 == "3":
            print("")
            sel7 = input(
                "..........\n"
                "1. \u20A62500 = 50MB 3 Days\n"
                "2. \u20A65000 = 125MB 7 Days\n"
                "3. \u20A610000 = 1GB 10 Days\n"
                "4. \u20A625000 = 2.5GB 30 Days\n"
                "5. \u20A650000 = 6GB 60 Days\n"
                "6. List of countries & partners\n"
                "Please select an option: "
            )
            if sel7 == "1":
                print("You have successfully activated 50MB, valid for 3 days")
            elif sel7 == "2":
                print("You have successfully activated 125MB, valid for 7 days")
            elif sel7 == "3":
                print("You have successfully activated 1GB, valid for 10 days")
            elif sel7 == "4":
                print("You have successfully activated 2.5GB, valid for 30 days")
            elif sel7 == "5":
                print("You have successfully activated 6GB, valid for 60 days")
            elif sel7 == "6":
                print("")
                print("UAE - Etisalat, Ghana - Millicom. UK - H3G. USA - Tmobile. USA - AT&T. USA - Limitless. France - Orange.")
                print("Saudi Arabia - Saudi Telecom, Kenya - Safaricom. Turkey - Avea. Italy - Telecom Italia. India - Vodafoneidea.")
                print("South Africa - Telkcom. Netherlands - KPN. Switzerland Swisscom. Switzerland - Orange. Belgium - Mobistar.")
                print("Poland - Polkomtel. Luxemborg - Orange. Sweden - Tel2. Cyprus - Areeba. Estonia - Tele2. Ireland - Meteor.")
                print("Ireland - H3G. Malta - Salt. Srilanka - Hutchison. Srilanka - Etisalat. Hongkong - PCCW. Hongkong - H3G. ")
                print("Iceland - Simmin. Liechteinstein - Salt. Indonesia - IND Telkomsel. Isreal - IL Pelephone. Macau - CTM. Iran - MCI.")
                print("Sudan - Zain. Brazil - Claro. Dominican - Claro. Equador - Claro. Nicaragua - Claro. Peru - Claro. Puerto Rico - Claro")
                print("Argentina - Claro. Andorra - Orange. Monaco - Orange. San Marino - TIM")
            else:
                print("Invalid option")
        elif sel2 == "4":
            print("")
            sel8 = input(
                "..........\n"
                "Get 10 times value of all your recharges with GLO TALK ON. To migrate:\n"
                "1. Glo Talk On\n"
                "Please select an option: "
            )
            if sel8 == "1":
                print("Sorry, the ussd command you sent is not valid")
            else:
                print("Invalid option")
        elif sel2 == "5":
            print("")
            sel9 = input(
                "..........\n"
                "Get 10 times value of all your recharges with GLO SUPER TALK. To migrate:\n"
                "1. Glo Super Talk\n"
                "Please select an option: "
            )
            if sel9 == "1":
                print("Sorry, the ussd command you sent is not valid")
            else:
                print("Invalid option")
        elif sel2 == "6":
            print("Your request for ALWAYS ON subscription is being processed. Please dial #100# after 2hrs for confirmation.")
            print("A fee of \u20A6500 is charged for this service")
        else:
            print("Invalid option")
    elif options == "11":
        print("")
        sel7 = input(
            "..........\n"
            "1. Call Center/Help Desk: 300\n"
            "2. SIM reg Verification: *996#\n"
            "3. DND Services: 2442\n"
            "4. MNP: 3232\n"
            "5. Data Roaming Offers\n"
            "Please select an option: "
        )
        if sel7 == "1":
            print("Dear Customer, please dial *300# to reach out to Glo Customer Care")
        elif sel7 == "2":
            print("Dear Customer, please dial *996# for SIM Reg details")
        elif sel7 == "3":
            print("Dear Customer, please SMS DND to 2442, to opt out promotional SMS")
        elif sel7 == "4":
            print("Dear Customer for MNP service, please send PORT TO 3232")
        elif sel7 == "5":
            print("")
            sel7 = input(
                "..........\n"
                "1. \u20A62500 = 50MB 3 Days\n"
                "2. \u20A65000 = 125MB 7 Days\n"
                "3. \u20A610000 = 1GB 10 Days\n"
                "4. \u20A625000 = 2.5GB 30 Days\n"
                "5. \u20A650000 = 6GB 60 Days\n"
                "6. List of countries & partners\n"
                "Please select an option: "
            )
            if sel7 == "1":
                print("")
                print("You have successfully activated 50MB, valid for 3 days")
            elif sel7 == "2":
                print("You have successfully activated 125MB, valid for 7 days")
            elif sel7 == "3":
                print("You have successfully activated 1GB, valid for 10 days")
            elif sel7 == "4":
                print("You have successfully activated 2.5GB, valid for 30 days")
            elif sel7 == "5":
                print("You have successfully activated 6GB, valid for 60 days")
            elif sel7 == "6":
                print("")
                print("UAE - Etisalat, Ghana - Millicom. UK - H3G. USA - Tmobile. USA - AT&T. USA - Limitless. France - Orange.")
                print("Saudi Arabia - Saudi Telecom, Kenya - Safaricom. Turkey - Avea. Italy - Telecom Italia. India - Vodafoneidea.")
                print("South Africa - Telkcom. Netherlands - KPN. Switzerland Swisscom. Switzerland - Orange. Belgium - Mobistar.")
                print("Poland - Polkomtel. Luxemborg - Orange. Sweden - Tel2. Cyprus - Areeba. Estonia - Tele2. Ireland - Meteor.")
                print("Ireland - H3G. Malta - Salt. Srilanka - Hutchison. Srilanka - Etisalat. Hongkong - PCCW. Hongkong - H3G. ")
                print("Iceland - Simmin. Liechteinstein - Salt. Indonesia - IND Telkomsel. Isreal - IL Pelephone. Macau - CTM. Iran - MCI.")
                print("Sudan - Zain. Brazil - Claro. Dominican - Claro. Equador - Claro. Nicaragua - Claro. Peru - Claro. Puerto Rico - Claro")
                print("Argentina - Claro. Andorra - Orange. Monaco - Orange. San Marino - TIM")
            else:
                print("Invalid option")
        else:
            print("Invalid option")
    else:
        print("Invalid option")
else:
    print("Invalid code")

import time
def play():
    print("############ WELCOME TO VISUAL FALKS############")
    print("\n")
    print("tell us what artworks would you like to do?")
    print("\n")
    print("1-Oil Colours")
    print("2 -Acrylic Colours")
    print("3 -Water Colours")
    print("3 -Charcoals")
    print("4 -Soft Pastels")
    print("5 -Drawing Pencils")
    print("6 -Exit")
    print("\n")
    c=int(input("choose your section "))

    if c==1:
        d = {1: 'Landscape painting ', 2: 'Seascape painting', 3: 'Still life painting', 4: 'Figure painting',
             5: 'Self-portrait painting', 6: 'Painting portraits of your friends and family', 7: 'Painting animals',
             8: 'Dreams, fantasy, mythological, allegorical and imaginary painting'}
        print("**********************************************************************************")
        print("\n")
        print("1=> Landscape painting ")
        print("2=> Seascape painting")
        print("3=> Still life painting")
        print("4=> Figure painting")
        print("5=> Self-portrait painting")
        print("6=> Painting portraits of your friends and family")
        print("7=> Painting animals")
        print("8=>Dreams, fantasy, mythological, allegorical and imaginary painting")
        print("\n")
        z=int(input("select your topic "))
        print("**********************************************************************************")
        print("topic: ",d[z])
        o=str(input("how many time did you want (hvr:min) :"))
        x=input("presss @ button to start")
        if x=='@':
            print("************** Best Wishes **************")
            l=o.split(':')
            h=int(l[0])
            m=int(l[1])
            s = h * 60
            for i in range(s+1):
                if h < 10 and m < 10:
                    print(f'0{h}:0{m}')
                elif h < 10 and m >= 10:
                    print(f'0{h}:{m}')
                elif h >= 10 and m < 10:
                    print(f'{h}:0{m}')
                elif h >= 10 and m >= 10:
                    print(f'{h}:{m}')
                time.sleep(60)  # print each element afer a time delay
                if m == 0:
                    m = 60
                    h = h - 1
                m = m - 1
            print("your time ends now")
            x=input("upload your creativity :")
            print("\n")
            print("******* congratulation you are successfully compleated the task *******")
            print("\n")
            print("\n")
            x=input("press enter button to go back")
            play()

    if c==2:
        d = {1: 'Color Block Design', 2: 'Geometric Galaxy', 3: ' Cheery Donuts', 4: 'Colorful Pineapple',
             5: ' Shaded Lane', 6: 'Autumn Forest', 7: ' Rainbow Swirly Tree',
             8: 'Bouquet of Flowers'}
        print("**********************************************************************************")
        print("\n")
        print("1=> Color Block Design ")
        print("2=> Geometric Galaxy")
        print("3=> Cheery Donuts")
        print("4=> Colorful Pineapple")
        print("5=> Shaded Lane")
        print("6=> Autumn Forest")
        print("7=> Rainbow Swirly Tree")
        print("8=>Bouquet of Flowers")
        print("\n")
        z = int(input("select your topic "))
        print("**********************************************************************************")
        print("topic: ", d[z])
        o = str(input("how many time did you want (hvr:min) :"))
        x = input("presss @ button to start")
        if x == '@':
            print("************** Best Wishes **************")
            l = o.split(':')
            h = int(l[0])
            m = int(l[1])
            s = h * 60
            for i in range(s + 1):
                if h < 10 and m < 10:
                    print(f'0{h}:0{m}')
                elif h < 10 and m >= 10:
                    print(f'0{h}:{m}')
                elif h >= 10 and m < 10:
                    print(f'{h}:0{m}')
                elif h >= 10 and m >= 10:
                    print(f'{h}:{m}')
                time.sleep(60)  # print each element afer a time delay
                if m == 0:
                    m = 60
                    h = h - 1
                m = m - 1
            print("your time ends now")
            x = input("upload your creativity :")
            print("******* congratulation you are successfully compleated the task *******")
            x = input("press enter button to go back")
            play()
    if c==3:
        d = {1: 'Watercolor Sketchbooks', 2: 'Galaxies', 3: ' Colorful Peacock', 4: ' Butterflies',
             5: ' Garden Vegetables', 6: ' Shaded Donuts', 7: ' Fall Leaves',
             8: ' Delicate Roses'}
        print("**********************************************************************************")
        print("\n")
        print("1=> Watercolor Sketchbooks ")
        print("2=> Galaxies")
        print("3=> Colorful Peacock")
        print("4=> Butterflies")
        print("5=> Garden Vegetables")
        print("6=> Shaded Donuts")
        print("7=> Fall Leaves")
        print("8=>Delicate Roses")
        print("\n")
        z = int(input("select your topic "))
        print("**********************************************************************************")
        print("topic: ", d[z])
        o = str(input("how many time did you want (hvr:min) :"))
        x = input("presss @ button to start")
        if x == '@':
            print("************** Best Wishes **************")
            l = o.split(':')
            h = int(l[0])
            m = int(l[1])
            s = h * 60
            for i in range(s + 1):
                if h < 10 and m < 10:
                    print(f'0{h}:0{m}')
                elif h < 10 and m >= 10:
                    print(f'0{h}:{m}')
                elif h >= 10 and m < 10:
                    print(f'{h}:0{m}')
                elif h >= 10 and m >= 10:
                    print(f'{h}:{m}')
                time.sleep(60)  # print each element afer a time delay
                if m == 0:
                    m = 60
                    h = h - 1
                m = m - 1
            print("your time ends now")
            x = input("upload your creativity :")
            print("******* congratulation you are successfully compleated the task *******")
            x = input("press enter button to go back")
            play()

    if c==4:
        d = {1: 'Beach Flowers', 2: 'Landscape ', 3: 'Sunset Drawing Over the Wheat Field', 4: ' Galaxy',
             5: ' Dramatic Sunset', 6: ' Tonal Sky', 7: ' Bird Soft',
             8: ' Autumn Leaf'}
        print("**********************************************************************************")
        print("\n")
        print("1=> Beach Flowers ")
        print("2=> Landscape ")
        print("3=> Sunset Drawing Over the Wheat Field")
        print("4=> Galaxy")
        print("5=> Dramatic Sunset")
        print("6=>  Tonal Sky")
        print("7=> Bird Soft")
        print("8=>Autumn Leaf")
        print("\n")
        z = int(input("select your topic "))
        print("**********************************************************************************")
        print("topic: ", d[z])
        o = str(input("how many time did you want (hvr:min) :"))
        x = input("presss @ button to start")
        if x == '@':
            print("************** Best Wishes **************")
            l = o.split(':')
            h = int(l[0])
            m = int(l[1])
            s = h * 60
            for i in range(s + 1):
                if h < 10 and m < 10:
                    print(f'0{h}:0{m}')
                elif h < 10 and m >= 10:
                    print(f'0{h}:{m}')
                elif h >= 10 and m < 10:
                    print(f'{h}:0{m}')
                elif h >= 10 and m >= 10:
                    print(f'{h}:{m}')
                time.sleep(60)  # print each element afer a time delay
                if m == 0:
                    m = 60
                    h = h - 1
                m = m - 1
            print("your time ends now")
            x = input("upload your creativity :")
            print("******* congratulation you are successfully compleated the task *******")
            x = input("press enter button to go back")
            play()
    if c==5:
        d = {1: 'The interior of your living room', 2: 'Kitchen utensils, like a whisk or slotted spoon', 3: 'A necklace, ring, or another piece of jewelry—try combining them in a still life', 4: ' House keys attached to a keychain',
             5: ' An interesting knick-knack (or knick-knacks) off your shelf', 6: ' An interesting doorknob or door knocker', 7: ' Crumpled fabric or a pile of laundry',
             8: ' An object in a glass dish'}
        print("**********************************************************************************")
        print("\n")
        print("1=> The interior of your living room ")
        print("2=> Kitchen utensils, like a whisk or slotted spoon ")
        print("3=> A necklace, ring, or another piece of jewelry—try combining them in a still life")
        print("4=> House keys attached to a keychain")
        print("5=> An interesting knick-knack (or knick-knacks) off your shelf")
        print("6=> An interesting doorknob or door knocker")
        print("7=> Crumpled fabric or a pile of laundry")
        print("8=> An object in a glass dish")
        print("\n")
        z = int(input("select your topic "))
        print("**********************************************************************************")
        print("topic: ", d[z])
        o = str(input("how many time did you want (hvr:min) :"))
        x = input("presss @ button to start")
        if x == '@':
            print("************** Best Wishes **************")
            l = o.split(':')
            h = int(l[0])
            m = int(l[1])
            s = h * 60
            for i in range(s + 1):
                if h < 10 and m < 10:
                    print(f'0{h}:0{m}')
                elif h < 10 and m >= 10:
                    print(f'0{h}:{m}')
                elif h >= 10 and m < 10:
                    print(f'{h}:0{m}')
                elif h >= 10 and m >= 10:
                    print(f'{h}:{m}')
                time.sleep(60)  # print each element afer a time delay
                if m == 0:
                    m = 60
                    h = h - 1
                m = m - 1
            print("your time ends now")
            x = input("upload your creativity :")
            print("******* congratulation you are successfully compleated the task *******")
            x = input("press enter button to go back")
            play()
    if c==6:
        d = input("press space and enter button to go home page")
        if d == " ":
            from frnd import f
            f()


play()
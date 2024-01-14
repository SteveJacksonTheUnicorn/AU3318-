from config import *

def draw_signal(sig, pics):
    print("iter ", pics)
    x = np.linspace(0,len(sig)/(sampling_rate/1000)-1,len(sig))
    plt.figure(figsize=(24,8))
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.plot(x,sig)
    plt.title("松紧度为{}时的第{}次敲击的时域图像".format(name,pics),fontsize=24)
    plt.xlabel("Time/(ms)", fontdict={'family' : 'Times New Roman'}, fontsize=20)
    plt.ylabel("Amplitude/(mV)",fontdict={'family' : 'Times New Roman'}, fontsize=20)
    plt.xticks(fontproperties='Times New Roman', fontsize=20)
    plt.yticks(fontproperties='Times New Roman', fontsize=20)
    plt.savefig("{}raw/interval {}.png".format(name,pics))
    plt.close()

if __name__ == "__main__":
    for num in range(1,11):
        # if num <= 9:
        #     continue
        name = num*400
        print("\n{}raw".format(name))
        if not os.path.exists("{}raw".format(name)):
            os.makedirs("{}raw".format(name))
        else:
            shutil.rmtree("{}raw".format(name))
            os.makedirs("{}raw".format(name))
        if not os.path.exists("{}rawtxt".format(name)):
            os.makedirs("{}rawtxt".format(name))
        else:
            shutil.rmtree("{}rawtxt".format(name))
            os.makedirs("{}rawtxt".format(name))

        left = [-1]
        right = [-1]

        datafile = "data/{}raw.mat".format(name)
        data = scio.loadmat(datafile)
        sig0 = data['data']
        l,w = sig0.shape

        # Compute the amplicude by adding the window
        ampli = np.empty((l,))
        for i in range(l-frames+1):
            ampli[i] = np.sum(np.abs(sig0[i:i+frames])) / frames
        for i in range(l-frames+1,l):
            ampli[i] = np.sum(np.abs(sig0[i:l])) / (l-i)
        x = np.linspace(0,len(ampli)-1,len(ampli))
        plt.plot(x,ampli)
        plt.savefig("{}raw/ampli.png".format(name))
        plt.close()

        print("finding intervals...")
        for i in range(l):
            if ampli[i] > thres and len(left) == len(right):
                left.append(i)
            elif ampli[i] < thres and len(left) > len(right):
                right.append(i)

        print("visualizing...")
        pics = 1
        l, r = -1, -1

        for i in range(1,len(left)):
            print("{}/{}".format(i,len(left)-1))
            if l == -1:
                l,r = left[i],right[i]
            elif r+length/2 > left[i]-length/2:
                r = right[i]
            else:
                result = sig0[l-50:l+length-50]
                draw_signal(result, pics)
                np.savetxt("{}rawtxt/interval_{}.txt".format(name,pics), result)
                pics += 1
                l,r = left[i],right[i]
        
        result = sig0[l-50:l+length-50]
        draw_signal(result, pics)
        np.savetxt("{}rawtxt/interval_{}.txt".format(name,pics), result)
        # if num == 2:
        #     break

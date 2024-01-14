from config import *

def extract_freq(wave):
    xf = np.fft.rfft(wave, n=fft_size, axis=0)/length*2
    return np.abs(xf)

def extract():
    if not os.path.exists(os.path.join(mission_path, "FFT=2^{}".format(int(np.log2(fft_size))))):
        os.makedirs(os.path.join(mission_path, "FFT=2^{}".format(int(np.log2(fft_size)))))
    else:
        shutil.rmtree(os.path.join(mission_path, "FFT=2^{}".format(int(np.log2(fft_size)))))
        os.makedirs(os.path.join(mission_path, "FFT=2^{}".format(int(np.log2(fft_size)))))

    for num in range(1,11):
        # if num == 1:
        #     continue
        name = num*400
        print("{}raw".format(name))
        path_ = "separated_signals/{}rawtxt".format(name)
        fs = np.linspace(0, sampling_rate/2, fft_size//2+1)
        plt.figure(figsize=(12,4))
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        wave = np.zeros(fft_size//2+1, dtype=np.float32)
        a = 1
        for sigfile in os.listdir(path_):
            sig = np.loadtxt(os.path.join(path_, sigfile), dtype=np.float32)
            
            # # pre-emphasis
            # a = 0.97
            # xn = sig+[0]
            # xn_1 = [0]+sig
            # sig = [xn[i]-a*xn_1[i] for i in range(len(xn))][:-1]
            wave = extract_freq(sig)
            
            plt.plot(fs, wave, linewidth=1)
            plt.xlabel(u"f(Hz)",fontsize=6)
            plt.ylabel(u'|P1(f)|',fontsize=6)
            plt.tick_params(labelsize=5)
            plt.title("松紧度为{}时的第{}幅 单侧幅值频谱图".format(name, a),fontsize=6)
            plt.savefig(os.path.join(mission_path, "FFT=2^{}".format(int(np.log2(fft_size))), "{}raw_interval_{}.png".format(name,a)))
            plt.close()
            np.savetxt(os.path.join(mission_path, "FFT=2^{}".format(int(np.log2(fft_size))), "{}raw_interval_{}.txt".format(name,a)), wave)
            a += 1

        # wave /= len(os.listdir(path_))
        # plt.plot(fs, wave, linewidth=0.6)
        # plt.xlabel(u"f(Hz)",fontsize=6)
        # plt.ylabel(u'|P1(f)|',fontsize=6)
        # plt.tick_params(labelsize=5)
        # plt.title("松紧度为{}时的共{}幅 单侧幅值频谱平均值".format(name,len(os.listdir(path_))),fontsize=6)
        # plt.show()
        # plt.savefig(os.path.join(mission_path, "FFT=2^{}".format(int(np.log2(fft_size))), "{}raw.png".format(name)))
        # plt.close()
        # np.savetxt(os.path.join(mission_path, "FFT=2^{}".format(int(np.log2(fft_size))), "{}raw.txt".format(name)), wave)
        # if num == 2:
        #     break

def features():
    for num in range(1,11):
        if num == 1:
            continue
        name = num*400
        print("{}raw".format(name))
        path_ = "f_analysis_average/FFT=2^14/{}raw.txt".format(name)
        freq = np.loadtxt(path_, dtype=np.float32)
        diff = np.diff(freq, prepend=0)
        peak = []
        for i in range(1,len(diff)-1):
            if diff[i] > 0 and diff[i+1] < 0:
                peak.append(i)
        print("peak: {}".format(peak))
        if num == 2:
            break


if __name__ == "__main__":
    mission_path = "f_analysis"
    extract() # 时域转频域
    
    # features() # 特征提取
    
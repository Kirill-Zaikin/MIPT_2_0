import numpy as np
import matplotlib.pyplot as plt
def task_3_2(variant):
    nu_c1 = [0.2, 0.15, 0.15, 0.1, 0.15, 0.15, 0.2, 0.15, 0.15, 0.1]
    amp1 = [1,  0, 0.2, 1, 1, 0.6, 0.3, 0.2, 1, 1]
    nu_c2 = [0.4, 0.35, 0.4,  0.3,  0.35,  0.4, 0.4,  0.3,  0.35,  0.4]
    amp2 = [0.4, 1, 1, 0.4, 0.7,  1, 1, 1, 0.4, 0.7]
    def H_val(nu, n):
        return amp1[n] if abs(nu)<=nu_c1[n] else amp2[n] if abs(nu)<=nu_c2[n] else 0.0
    nu=np.arange(-0.5, 0.5, 0.001)
    plt.figure(figsize=[6, 2], dpi=140)
    plt.plot(nu, [H_val(x, variant-1) for x in nu] ,'g-')
    plt.xticks([-0.5, -nu_c2[variant-1], -nu_c1[variant-1], 0, nu_c1[variant-1], nu_c2[variant-1], 0.5])
    plt.grid()
    plt.yticks([0, min(amp1[variant-1],amp2[variant-1]), 1])
    plt.xlim([-0.5, 0.5])
    plt.xlabel("Нормированнная частота, $\\nu$")
    plt.ylabel("$H(\\nu)$")
    plt.title("Вариант %i" %variant)
    plt.tight_layout()
    plt.show()
    return np.array([H_val(x, variant-1) for x in nu])

H = task_3_2(variant=5)
h_ideal = np.fft.fftshift(np.fft.ifft(np.fft.ifftshift(H)))

plt.figure(figsize=(10, 3))
k = np.arange(-len(h_ideal) / 2, len(h_ideal) / 2)
plt.plot(k, np.abs(np.real(h_ideal)), label='$h_{ideal}[k]$')
plt.title(f'h[k]')
plt.xlabel('$k$')
plt.ylabel('$h[k]$')
plt.grid(); plt.legend(); plt.show()

N = 50
new_h = h_ideal[int(len(h_ideal)/2) - N:int(len(h_ideal)/2) + N]

plt.figure(figsize=(10, 3))
k = np.arange(- N, N)
plt.stem(k, np.abs(np.real(new_h)), label='$h_{ideal}[k]$')
plt.title(f'h[k]')
plt.xlabel('$k$')
plt.ylabel('$h[k]$')
plt.grid(); plt.legend(); plt.show()

plt.figure(figsize=(10, 3))
nu = np.linspace(-0.5, 0.5, 1024)
plt.plot(nu, np.abs(np.fft.fftshift(np.fft.fft(new_h, 1024))), label='$H(\\nu)$')
plt.title('$H(\\nu)$')
plt.xlabel('$\\nu$')
plt.ylabel('$H(\\nu)$')
plt.grid(); plt.legend(); plt.show()
from grid import Grid
import numpy as np


class Simulation(object):
    def __init__(
            self,
            grid_x: Grid,
            grid_p: Grid,
            grid_t: Grid,
    ):
        self.x = grid_x
        self.p = grid_p
        self.t = grid_t

        # Gaussian wavepacket with 'zero' momentum
        self.wf = (np.exp(-((self.x.space-1) ** 2) / 2) *
                   np.exp(1j * np.min(self.p.mid_space * self.x.space)))
        self.wf_p = None

        self.v = self.x.space ** 2

        self.wf_t = [self.wf]

    @property
    def dt(self):
        return self.t.d

    @property
    def dx(self):
        return self.x.d

    @property
    def dp(self):
        return self.p.d

    @property
    def norm(self):
        return np.trapz(np.abs(self.wf) ** 2, x=self.x.space)

    @property
    def x_op(self):
        return np.trapz(self.x.space * np.abs(self.wf) ** 2, x=self.x.space)

    @property
    def p_op(self):
        # FFT to momentum space
        self.wf_p = np.fft.fft(self.wf)
        self.wf_p = np.fft.fftshift(self.wf_p)
        # P operator
        self.wf_p *= self.p.space
        # Inverse FFT back to position space
        self.wf_p = np.fft.ifftshift(self.wf_p)
        wfp = np.fft.ifft(self.wf_p)

        return np.trapz(np.abs(wfp) ** 2, x=self.x.space)

    def normalize(self):
        self.wf /= np.sqrt(self.norm)

    def simulate(self):
        for _ in self.t.space:
            # Half-step in position space
            self.wf *= np.exp(-1j * self.v * self.dt / 2)

            # FFT to momentum space
            self.wf_p = np.fft.fft(self.wf)
            self.wf_p = np.fft.fftshift(self.wf_p)

            # Full step in momentum space
            self.wf_p *= np.exp(-1j * (self.p.space ** 2) * self.dt / 2)

            # Inverse FFT back to position space
            self.wf_p = np.fft.ifftshift(self.wf_p)
            self.wf = np.fft.ifft(self.wf_p)

            # Half-step in position space
            self.wf *= np.exp(-1j * self.v * self.dt / 2)

            self.normalize()
            print(f"t: {_}, norm: {self.norm}")

            self.wf_t.append(self.wf)

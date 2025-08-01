from importlib.metadata import version

__version__ = version(__name__)
del version

import functools
import sys
import types

from .usertools import monitor, timing

from .ctx_fp import FPContext
from .ctx_mp import MPContext
from .ctx_iv import MPIntervalContext

# deprecated modules
from . import rational
from . import math2

fp = FPContext()
mp = MPContext()
iv = MPIntervalContext()

fp._mp = mp
mp._mp = mp
iv._mp = mp
mp._fp = fp
fp._fp = fp
mp._iv = iv
fp._iv = iv
iv._iv = iv

make_mpf = mp.make_mpf
make_mpc = mp.make_mpc

extraprec = mp.extraprec
extradps = mp.extradps
workprec = mp.workprec
workdps = mp.workdps
autoprec = mp.autoprec
maxcalls = mp.maxcalls
memoize = mp.memoize

mag = mp.mag

bernfrac = mp.bernfrac

qfrom = mp.qfrom
mfrom = mp.mfrom
kfrom = mp.kfrom
taufrom = mp.taufrom
qbarfrom = mp.qbarfrom
ellipfun = mp.ellipfun
jtheta = mp.jtheta
kleinj = mp.kleinj
eta = mp.eta

qp = mp.qp
qhyper = mp.qhyper
qgamma = mp.qgamma
qfac = mp.qfac

nint_distance = mp.nint_distance

plot = mp.plot
cplot = mp.cplot
splot = mp.splot

odefun = mp.odefun

jacobian = mp.jacobian
findroot = mp.findroot
multiplicity = mp.multiplicity

isinf = mp.isinf
isnan = mp.isnan
isnormal = mp.isnormal
isspecial = mp.isspecial
isint = mp.isint
isfinite = mp.isfinite
almosteq = mp.almosteq
nan = mp.nan
rand = mp.rand

absmin = mp.absmin
absmax = mp.absmax

fraction = mp.fraction

linspace = mp.linspace
arange = mp.arange

mpmathify = convert = mp.convert
mpc = mp.mpc

mpi = iv._mpi

nstr = mp.nstr
nprint = mp.nprint
chop = mp.chop

fneg = mp.fneg
fadd = mp.fadd
fsub = mp.fsub
fmul = mp.fmul
fdiv = mp.fdiv
fprod = mp.fprod

quad = mp.quad
quadgl = mp.quadgl
quadts = mp.quadts
quadosc = mp.quadosc
quadsubdiv = mp.quadsubdiv

invertlaplace = mp.invertlaplace
invlaptalbot = mp.invlaptalbot
invlapstehfest = mp.invlapstehfest
invlapdehoog = mp.invlapdehoog

pslq = mp.pslq
identify = mp.identify
findpoly = mp.findpoly

richardson = mp.richardson
shanks = mp.shanks
levin = mp.levin
cohen_alt = mp.cohen_alt
nsum = mp.nsum
nprod = mp.nprod
difference = mp.difference
diff = mp.diff
diffs = mp.diffs
diffs_prod = mp.diffs_prod
diffs_exp = mp.diffs_exp
diffun = mp.diffun
differint = mp.differint
taylor = mp.taylor
pade = mp.pade
polyval = mp.polyval
polyroots = mp.polyroots
fourier = mp.fourier
fourierval = mp.fourierval
sumem = mp.sumem
sumap = mp.sumap
chebyfit = mp.chebyfit
limit = mp.limit

matrix = mp.matrix
eye = mp.eye
diag = mp.diag
zeros = mp.zeros
ones = mp.ones
hilbert = mp.hilbert
randmatrix = mp.randmatrix
swap_row = mp.swap_row
extend = mp.extend
norm = mp.norm
mnorm = mp.mnorm

lu_solve = mp.lu_solve
lu = mp.lu
qr = mp.qr
unitvector = mp.unitvector
inverse = mp.inverse
residual = mp.residual
qr_solve = mp.qr_solve
cholesky = mp.cholesky
cholesky_solve = mp.cholesky_solve
det = mp.det
cond = mp.cond
hessenberg = mp.hessenberg
schur = mp.schur
eig = mp.eig
eig_sort = mp.eig_sort
eigsy = mp.eigsy
eighe = mp.eighe
eigh = mp.eigh
svd_r = mp.svd_r
svd_c = mp.svd_c
svd = mp.svd
gauss_quadrature = mp.gauss_quadrature
rank = mp.rank

expm = mp.expm
sqrtm = mp.sqrtm
powm = mp.powm
logm = mp.logm
sinm = mp.sinm
cosm = mp.cosm

mpf = mp.mpf
j = mp.j
exp = mp.exp
expj = mp.expj
expjpi = mp.expjpi
ln = mp.ln
im = mp.im
re = mp.re
inf = mp.inf
ninf = mp.ninf
sign = mp.sign

eps = mp.eps
pi = mp.pi
ln2 = mp.ln2
ln10 = mp.ln10
exp2 = mp.exp2
log2 = mp.log2
phi = mp.phi
e = mp.e
euler = mp.euler
catalan = mp.catalan
khinchin = mp.khinchin
glaisher = mp.glaisher
apery = mp.apery
degree = mp.degree
twinprime = mp.twinprime
mertens = mp.mertens

ldexp = mp.ldexp
frexp = mp.frexp

fsum = mp.fsum
fdot = mp.fdot

sqrt = mp.sqrt
cbrt = mp.cbrt
exp = mp.exp
ln = mp.ln
log = mp.log
log10 = mp.log10
power = mp.power
cos = mp.cos
sin = mp.sin
tan = mp.tan
cosh = mp.cosh
sinh = mp.sinh
tanh = mp.tanh
acos = mp.acos
asin = mp.asin
atan = mp.atan
asinh = mp.asinh
acosh = mp.acosh
atanh = mp.atanh
sec = mp.sec
csc = mp.csc
cot = mp.cot
sech = mp.sech
csch = mp.csch
coth = mp.coth
asec = mp.asec
acsc = mp.acsc
acot = mp.acot
asech = mp.asech
acsch = mp.acsch
acoth = mp.acoth
cospi = mp.cospi
sinpi = mp.sinpi
sinc = mp.sinc
sincpi = mp.sincpi
cos_sin = mp.cos_sin
cospi_sinpi = mp.cospi_sinpi
fabs = mp.fabs
re = mp.re
im = mp.im
conj = mp.conj
floor = mp.floor
ceil = mp.ceil
nint = mp.nint
frac = mp.frac
root = mp.root
nthroot = mp.nthroot
hypot = mp.hypot
fmod = mp.fmod
ldexp = mp.ldexp
frexp = mp.frexp
sign = mp.sign
arg = mp.arg
phase = mp.phase
polar = mp.polar
rect = mp.rect
degrees = mp.degrees
radians = mp.radians
atan2 = mp.atan2
fib = mp.fib
fibonacci = mp.fibonacci
lambertw = mp.lambertw
zeta = mp.zeta
altzeta = mp.altzeta
gamma = mp.gamma
rgamma = mp.rgamma
factorial = mp.factorial
fac = mp.fac
fac2 = mp.fac2
beta = mp.beta
betainc = mp.betainc
psi = mp.psi
#psi0 = mp.psi0
#psi1 = mp.psi1
#psi2 = mp.psi2
#psi3 = mp.psi3
polygamma = mp.polygamma
digamma = mp.digamma
#trigamma = mp.trigamma
#tetragamma = mp.tetragamma
#pentagamma = mp.pentagamma
harmonic = mp.harmonic
bernoulli = mp.bernoulli
bernfrac = mp.bernfrac
stieltjes = mp.stieltjes
hurwitz = mp.hurwitz
dirichlet = mp.dirichlet
bernpoly = mp.bernpoly
eulerpoly = mp.eulerpoly
eulernum = mp.eulernum
polylog = mp.polylog
clsin = mp.clsin
clcos = mp.clcos
gammainc = mp.gammainc
lower_gamma = mp.lower_gamma
upper_gamma = mp.upper_gamma
gammaprod = mp.gammaprod
binomial = mp.binomial
rf = mp.rf
ff = mp.ff
hyper = mp.hyper
hyp0f1 = mp.hyp0f1
hyp1f1 = mp.hyp1f1
hyp1f2 = mp.hyp1f2
hyp2f1 = mp.hyp2f1
hyp2f2 = mp.hyp2f2
hyp2f0 = mp.hyp2f0
hyp2f3 = mp.hyp2f3
hyp3f2 = mp.hyp3f2
hyperu = mp.hyperu
hypercomb = mp.hypercomb
meijerg = mp.meijerg
foxh = mp.foxh
appellf1 = mp.appellf1
appellf2 = mp.appellf2
appellf3 = mp.appellf3
appellf4 = mp.appellf4
hyper2d = mp.hyper2d
bihyper = mp.bihyper
erf = mp.erf
erfc = mp.erfc
erfi = mp.erfi
erfinv = mp.erfinv
npdf = mp.npdf
ncdf = mp.ncdf
expint = mp.expint
e1 = mp.e1
ei = mp.ei
li = mp.li
ci = mp.ci
si = mp.si
chi = mp.chi
shi = mp.shi
fresnels = mp.fresnels
fresnelc = mp.fresnelc
airyai = mp.airyai
airybi = mp.airybi
airyaizero = mp.airyaizero
airybizero = mp.airybizero
scorergi = mp.scorergi
scorerhi = mp.scorerhi
ellipk = mp.ellipk
ellipe = mp.ellipe
ellipf = mp.ellipf
ellippi = mp.ellippi
elliprc = mp.elliprc
elliprj = mp.elliprj
elliprf = mp.elliprf
elliprd = mp.elliprd
elliprg = mp.elliprg
agm = mp.agm
jacobi = mp.jacobi
chebyt = mp.chebyt
chebyu = mp.chebyu
legendre = mp.legendre
legenp = mp.legenp
legenq = mp.legenq
hermite = mp.hermite
pcfd = mp.pcfd
pcfu = mp.pcfu
pcfv = mp.pcfv
pcfw = mp.pcfw
gegenbauer = mp.gegenbauer
laguerre = mp.laguerre
spherharm = mp.spherharm
besselj = mp.besselj
j0 = mp.j0
j1 = mp.j1
besseli = mp.besseli
bessely = mp.bessely
besselk = mp.besselk
besseljzero = mp.besseljzero
besselyzero = mp.besselyzero
spherical_jn = mp.spherical_jn
spherical_yn = mp.spherical_yn
hankel1 = mp.hankel1
hankel2 = mp.hankel2
struveh = mp.struveh
struvel = mp.struvel
angerj = mp.angerj
webere = mp.webere
lommels1 = mp.lommels1
lommels2 = mp.lommels2
whitm = mp.whitm
whitw = mp.whitw
ber = mp.ber
bei = mp.bei
ker = mp.ker
kei = mp.kei
coulombc = mp.coulombc
coulombf = mp.coulombf
coulombg = mp.coulombg
barnesg = mp.barnesg
superfac = mp.superfac
hyperfac = mp.hyperfac
loggamma = mp.loggamma
siegeltheta = mp.siegeltheta
siegelz = mp.siegelz
grampoint = mp.grampoint
zetazero = mp.zetazero
riemannr = mp.riemannr
primepi = mp.primepi
primepi2 = mp.primepi2
primezeta = mp.primezeta
bell = mp.bell
polyexp = mp.polyexp
expm1 = mp.expm1
log1p = mp.log1p
powm1 = mp.powm1
unitroots = mp.unitroots
cyclotomic = mp.cyclotomic
mangoldt = mp.mangoldt
secondzeta = mp.secondzeta
nzeros = mp.nzeros
backlunds = mp.backlunds
lerchphi = mp.lerchphi
stirling1 = mp.stirling1
stirling2 = mp.stirling2
squarew = mp.squarew
trianglew = mp.trianglew
sawtoothw = mp.sawtoothw
unit_triangle = mp.unit_triangle
sigmoid = mp.sigmoid


# Hack to guard against setting module properties instead of 'mp', Issue #657
class _MPMathModule(types.ModuleType):

    def _helper(self, *args, prop=''):
        raise AttributeError("cannot set '{name}' on 'mpmath'. Did you mean to "
                             "set '{name}' on 'mpmath.mp'?".format(name=prop))

    dps = property(fset=functools.partial(_helper, prop='dps'))
    prec = property(fset=functools.partial(_helper, prop='prec'))
    pretty = property(fset=functools.partial(_helper, prop='pretty'))
    trap_complex = property(fset=functools.partial(_helper, prop='trap_complex'))


sys.modules[__name__].__class__ = _MPMathModule
del functools, sys, types, _MPMathModule

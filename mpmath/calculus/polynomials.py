import warnings

from .calculus import defun


#----------------------------------------------------------------------------#
#                                Polynomials                                 #
#----------------------------------------------------------------------------#

# XXX: extra precision
@defun
def polyval(ctx, coeffs, x, derivative=False, asc=None):
    r"""
    Given coefficients `[c_0, c_1, c_2, \ldots, c_n]` and a number `x`,
    :func:`~mpmath.polyval` evaluates the polynomial

    .. math ::

        P(x) = c_0 + c_1 x + c_2 x^2 \ldots c_n x^n

    If *derivative=True* is set, :func:`~mpmath.polyval` simultaneously
    evaluates `P(x)` with the derivative, `P'(x)`, and returns the
    tuple `(P(x), P'(x))`.

        >>> from mpmath import mp, polyval
        >>> mp.pretty = True
        >>> polyval([2, 0, 3], 0.5, asc=True)
        2.75
        >>> polyval([2, 0, 3], 0.5, derivative=True, asc=True)
        (2.75, 3.0)

    If *asc=False*, descending order of coefficients is used (the term
    of largest degree - first).

    The coefficients and the evaluation point may be any combination
    of real or complex numbers.
    """
    if not coeffs:
        return ctx.zero
    if asc is None:
        warnings.warn("Descending (wrt powers) order of polynomial "
                      "coefficients is deprecated, please adapt your "
                      "code to use ascending order, asc=True.",
                      DeprecationWarning)
        asc = False
    if not asc:
        coeffs = coeffs[::-1]
    p = ctx.convert(coeffs[-1])
    q = ctx.zero
    for c in reversed(coeffs[:-1]):
        if derivative:
            q = p + x*q
        p = c + x*p
    if derivative:
        return p, q
    else:
        return p

@defun
def polyroots(ctx, coeffs, maxsteps=50, cleanup=True, extraprec=10,
              error=False, roots_init=None, asc=None):
    """
    Computes all roots (real or complex) of a given polynomial.

    The roots are returned as a sorted list, where real roots appear first
    followed by complex conjugate roots as adjacent elements. The polynomial
    should be given as a list of coefficients, in the format used by
    :func:`~mpmath.polyval`. The leading coefficient must be nonzero.

    With *error=True*, :func:`~mpmath.polyroots` returns a tuple *(roots, err)*
    where *err* is an estimate of the maximum error among the computed roots.

    If *asc=False*, descending order of coefficients is used (the term
    of largest degree - first).

    **Examples**

    Finding the three real roots of `x^3 - x^2 - 14x + 24`::

        >>> from mpmath import mp, polyroots, nprint, sqrt, polyval
        >>> mp.pretty = True
        >>> nprint(polyroots([24,-14,-1,1],asc=True), 4)
        [-4.0, 2.0, 3.0]

    Finding the two complex conjugate roots of `4x^2 + 3x + 2`, with an
    error estimate::

        >>> roots, err = polyroots([2,3,4], error=True, asc=True)
        >>> for r in roots:
        ...     print(r)
        ...
        (-0.375 + 0.59947894041409j)
        (-0.375 - 0.59947894041409j)
        >>>
        >>> err
        2.22044604925031e-16
        >>>
        >>> polyval([2,3,4], roots[0], asc=True)
        (2.22044604925031e-16 + 0.0j)
        >>> polyval([2,3,4], roots[1], asc=True)
        (2.22044604925031e-16 + 0.0j)

    The following example computes all the 5th roots of unity; that is,
    the roots of `x^5 - 1`::

        >>> mp.dps = 20
        >>> for r in polyroots([-1, 0, 0, 0, 0, 1], asc=True):
        ...     print(r)
        ...
        1.0
        (-0.8090169943749474241 + 0.58778525229247312917j)
        (-0.8090169943749474241 - 0.58778525229247312917j)
        (0.3090169943749474241 + 0.95105651629515357212j)
        (0.3090169943749474241 - 0.95105651629515357212j)

    **Precision and conditioning**

    The roots are computed to the current working precision accuracy. If this
    accuracy cannot be achieved in ``maxsteps`` steps, then a
    ``NoConvergence`` exception is raised. The algorithm internally is using
    the current working precision extended by ``extraprec``. If
    ``NoConvergence`` was raised, that is caused either by not having enough
    extra precision to achieve convergence (in which case increasing
    ``extraprec`` should fix the problem) or too low ``maxsteps`` (in which
    case increasing ``maxsteps`` should fix the problem), or a combination of
    both.

    The user should always do a convergence study with regards to
    ``extraprec`` to ensure accurate results. It is possible to get
    convergence to a wrong answer with too low ``extraprec``.

    Provided there are no repeated roots, :func:`~mpmath.polyroots` can
    typically compute all roots of an arbitrary polynomial to high precision::

        >>> mp.dps = 60
        >>> for r in polyroots([1, 0, -10, 0, 1], asc=True):
        ...     print(r)
        ...
        -3.14626436994197234232913506571557044551247712918732870123249
        -0.317837245195782244725757617296174288373133378433432554879127
        0.317837245195782244725757617296174288373133378433432554879127
        3.14626436994197234232913506571557044551247712918732870123249
        >>>
        >>> sqrt(3) + sqrt(2)
        3.14626436994197234232913506571557044551247712918732870123249
        >>> sqrt(3) - sqrt(2)
        0.317837245195782244725757617296174288373133378433432554879127

    **Algorithm**

    :func:`~mpmath.polyroots` implements the Durand-Kerner method [1], which
    uses complex arithmetic to locate all roots simultaneously.
    The Durand-Kerner method can be viewed as approximately performing
    simultaneous Newton iteration for all the roots. In particular,
    the convergence to simple roots is quadratic, just like Newton's
    method.

    Although all roots are internally calculated using complex arithmetic, any
    root found to have an imaginary part smaller than the estimated numerical
    error is truncated to a real number (small real parts are also chopped).
    Real roots are placed first in the returned list, sorted by value. The
    remaining complex roots are sorted by their real parts so that conjugate
    roots end up next to each other.

    **References**

    1. [Wikipedia]_ https://en.wikipedia.org/wiki/Durand-Kerner_method

    """
    if len(coeffs) <= 1:
        if not coeffs or not coeffs[0]:
            raise ValueError("Input to polyroots must not be the zero polynomial")
        # Constant polynomial with no roots
        return []

    if asc is None:
        warnings.warn("Descending (wrt powers) order of polynomial "
                      "coefficients is deprecated, please adapt you "
                      "code to use ascending order, asc=True.",
                      DeprecationWarning)
        asc = False
    if not asc:
        coeffs = coeffs[::-1]

    orig = ctx.prec
    tol = +ctx.eps
    with ctx.extraprec(extraprec):
        deg = len(coeffs) - 1
        # Must be monic
        lead = ctx.convert(coeffs[-1])
        if lead == 1:
            coeffs = [ctx.convert(c) for c in coeffs]
        else:
            coeffs = [c/lead for c in coeffs]
        f = lambda x: ctx.polyval(coeffs, x, asc=True)
        if roots_init is None:
            roots = [ctx.mpc((0.4+0.9j)**n) for n in range(deg)]
        else:
            roots = [None]*deg
            deg_init = min(deg, len(roots_init))
            roots[:deg_init] = list(roots_init[:deg_init])
            roots[deg_init:] = [ctx.mpc((0.4+0.9j)**n) for n
                                in range(deg_init,deg)]
        err = [ctx.one for n in range(deg)]
        # Durand-Kerner iteration until convergence
        for step in range(maxsteps):
            if abs(max(err)) < tol:
                break
            for i in range(deg):
                p = roots[i]
                x = f(p)
                for j in range(deg):
                    if i != j:
                        try:
                            x /= (p-roots[j])
                        except ZeroDivisionError:
                            continue
                roots[i] = p - x
                err[i] = abs(x)
        if abs(max(err)) >= tol:
            raise ctx.NoConvergence("Didn't converge in maxsteps=%d steps." \
                    % maxsteps)
        # Remove small real or imaginary parts
        if cleanup:
            for i in range(deg):
                if abs(roots[i]) < tol:
                    roots[i] = ctx.zero
                elif abs(ctx._im(roots[i])) < tol:
                    roots[i] = roots[i].real
                elif abs(ctx._re(roots[i])) < tol:
                    roots[i] = roots[i].imag * 1j
        roots.sort(key=lambda x: (abs(ctx._im(x)), ctx._re(x)))
    if error:
        err = max(err)
        err = max(err, ctx.ldexp(1, -orig+1))
        return [+r for r in roots], +err
    else:
        return [+r for r in roots]

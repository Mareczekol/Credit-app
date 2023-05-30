# data

kredyt = int(input("Podaj kwotę kredytu: "))
Miesieczna_rata = int(input("Podaj kwotę raty: "))
Oprocentowanie = float(input("Podaj oprocentowanie: "))/100
inflacja = [1.5928244841, -0.453509101, 2.324671717, 1.261254407, 1.782526286,
            2.329384541, 1.502229842, 1.782526286, 2.328848994, 0.616921348,
            2.352295886, 0.337779545, 1.577035247, -0.292781443, 2.48619659,
            0.267110318, 1.417952672, 1.054243267, 1.480520104, 1.577035247,
            -0.07742069, 1.165733399, -0.404186718, 1.499708521]


# Jan
a = (1 + ((inflacja[0] + 3)/1200)) * kredyt - Miesieczna_rata

wynik_finansowy = 'Twoja pozostała kwota kredytu to: {}'.format(a)
print(wynik_finansowy)

# TODO: write a formula for next calculations

# Feb
c = (1 + ((inflacja[1] + 3)/1200)) * a - Miesieczna_rata
d = a - c
print('Twoja pozostała kwota kredytu to: {} to: {} mniej niż w poprzednim '
      'miesiącu.'.format(c, d))

# Mar
e = (1 + ((inflacja[2] + 3)/1200)) * c - Miesieczna_rata
f = c - e
print('Twoja pozostała kwota kredytu to: {} to: {} mniej niż w poprzednim '
      'miesiącu.'.format(e, f))

# Apr
g = (1 + ((inflacja[3] + 3)/1200)) * e - Miesieczna_rata
h = e - g
print('Twoja pozostała kwota kredytu to: {} to: {} mniej niż w poprzednim '
      'miesiącu.'.format(g, h))

# May
i = (1 + ((inflacja[4] + 3)/1200)) * g - Miesieczna_rata
j = g - i
print('Twoja pozostała kwota kredytu to: {} to: {} mniej niż w poprzednim '
      'miesiącu.'.format(i, j))

# Jun
k = (1 + ((inflacja[5] + 3)/1200)) * i - Miesieczna_rata
l_2 = i - k
print('Twoja pozostała kwota kredytu to: {} to: {} mniej niż w poprzednim '
      'miesiącu.'.format(k, l_2))

# Jul
m = (1 + ((inflacja[6] + 3)/1200)) * k - Miesieczna_rata
n = k - m
print(('Twoja pozostała kwota kredytu to: {} to: {} mniej niż w poprzednim'
       ' miesiącu.'.format(m, n)))
# Aug
o = (1 + ((inflacja[7] + 3)/1200)) * m - Miesieczna_rata
p = m - o
print(('Twoja pozostała kwota kredytu to: {} to: {} mniej niż w poprzednim '
       'miesiącu.'.format(o, p)))
# Sep
r = (1 + ((inflacja[8] + 3)/1200)) * o - Miesieczna_rata
s = o - r
print(('Twoja pozostała kwota kredytu to: {} to: {} mniej niż w poprzednim '
      'miesiącu.'.format(r, s)))
# Oct
t = (1 + ((inflacja[9] + 3)/1200)) * r - Miesieczna_rata
u = r - t
print(('Twoja pozostała kwota kredytu to: {} to: {} mniej niż w poprzednim '
       'miesiącu.'.format(t, u)))
# Nov
w = (1 + ((inflacja[10] + 3)/1200)) * t - Miesieczna_rata
x = t - w
print(('Twoja pozostała kwota kredytu to: {} to: {} mniej niż w poprzednim '
       'miesiącu.'.format(w, x)))
# Dec
y = (1 + ((inflacja[11] + 3)/1200)) * w - Miesieczna_rata
z = w - y
print(('Twoja pozostała kwota kredytu to: {} to: {} mniej niż w poprzednim '
       'miesiącu.'.format(y, z)))
# Jan 2
a_1 = (1 + ((inflacja[12] + 3)/1200)) * y - Miesieczna_rata
b_1 = y - a_1
print(('Twoja pozostała kwota kredytu to: {} to: {} mniej niż w poprzednim '
       'miesiącu.'.format(a_1, b_1)))
# Feb 2
c_1 = (1 + ((inflacja[13] + 3)/1200)) * a_1 - Miesieczna_rata
d_1 = a_1 - c_1
print(('Twoja pozostała kwota kredytu to: {} to: {} mniej niż w poprzednim '
      'miesiącu.'.format(c_1, d_1)))
# Mar 2
e_1 = (1 + ((inflacja[14] + 3)/1200)) * c_1 - Miesieczna_rata
f_1 = c_1 - e_1
print(('Twoja pozostała kwota kredytu to: {} to: {} mniej niż w poprzednim '
       'miesiącu.'.format(e_1, f_1)))
# Apr 2
g_1 = (1 + ((inflacja[15] + 3)/1200)) * e_1 - Miesieczna_rata
h_1 = e_1 - g_1
print(('Twoja pozostała kwota kredytu to: {} to: {} mniej niż w poprzednim '
       'miesiącu.'.format(g_1, h_1)))
# May 2
i_1 = (1 + ((inflacja[16] + 3)/1200)) * g_1 - Miesieczna_rata
j_1 = g_1 - i_1
print(('Twoja pozostała kwota kredytu to: {} to: {} mniej niż w poprzednim '
       'miesiącu.'.format(i_1, j_1)))
# Jun 2
k_1 = (1 + ((inflacja[17] + 3)/1200)) * i_1 - Miesieczna_rata
l_1 = i_1 - k_1
print(('Twoja pozostała kwota kredytu to: {} to: {} mniej niż w poprzednim '
       'miesiącu.'.format(k_1, l_1)))
# Jul 2
m_1 = (1 + ((inflacja[18] + 3)/1200)) * k_1 - Miesieczna_rata
n_1 = k_1 - m_1
print(('Twoja pozostała kwota kredytu to: {} to: {} mniej niż w poprzednim '
      'miesiącu.'.format(m_1, n_1)))
# Aug 2
o_1 = (1 + ((inflacja[19] + 3)/1200)) * m_1 - Miesieczna_rata
p_1 = m_1 - o_1
print(('Twoja pozostała kwota kredytu to: {} to: {} mniej niż w poprzednim '
       'miesiącu.'.format(o_1, p_1)))
# Sep 2
r_1 = (1 + ((inflacja[20] + 3)/1200)) * o_1 - Miesieczna_rata
s_1 = o_1 - r_1
print(('Twoja pozostała kwota kredytu to: {} to: {} mniej niż w poprzednim '
       'miesiącu.'.format(r_1, s_1)))
# Oct 2
t_1 = (1 + ((inflacja[21] + 3)/1200)) * r_1 - Miesieczna_rata
u_1 = r_1 - t_1
print(('Twoja pozostała kwota kredytu to: {} to: {} mniej niż w poprzednim '
      'miesiącu.'.format(t_1, u_1)))
# Nov 2
w_1 = (1 + ((inflacja[22] + 3)/1200)) * t_1 - Miesieczna_rata
x_1 = t_1 - w_1
print(('Twoja pozostała kwota kredytu to: {} to: {} mniej niż w poprzednim '
       'miesiącu.'.format(w_1, x_1)))
# Dec 2
y_1 = (1 + ((inflacja[23] + 3)/1200)) * w_1 - Miesieczna_rata
z_1 = w_1 - y_1
print(('Twoja pozostała kwota kredytu to: {} to: {} mniej niż w poprzednim '
       'miesiącu.'.format(y_1, z_1)))

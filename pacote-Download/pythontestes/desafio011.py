al = float(input('Qual a altura da parede? '))
la = float(input('Qual a largura da parede? '))
area = al * la
t = area / 2
print('Sua parede tem dimensão de {}x{} e sua área é de {}m².'.format(al, la, area))
print('Serão necessários {:.2f} litros de tinta para a pintura da parede.'.format(t))

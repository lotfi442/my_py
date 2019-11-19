{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import math\n",
    "\n",
    "def calculerdelta(a,b,c)\n",
    "return b*b-4*a*c\n",
    "\n",
    "def resoudreequationseconddegrès(a,b,c)\n",
    "delta = calculerdelta(a, b, c)\n",
    "if delta > 0;\n",
    "racineDeDelta=math.sqrt(delta)retour = [(-b-racineDeDelta)/(2*a),(-b+racineDeDelta)/(2*a)]\n",
    "   elif delta < 0:\n",
    "      retour = []\n",
    "   else:\n",
    "      retour = [-b/(2*a)] \n",
    "   return retour\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "delta = ((-7)*(-7)) - 4 * (3)*(-23)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "325\n"
     ]
    }
   ],
   "source": [
    "print(delta)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "r = math.sqrt\n",
    "x1 = ((7)-r(118))/6\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-0.6437967485333692\n"
     ]
    }
   ],
   "source": [
    "print(x1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [],
   "source": [
    "x2=((7)+r(118))/6"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2.9771300818667026\n"
     ]
    }
   ],
   "source": [
    "print(x2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7997440\n",
      "16786472\n",
      "8\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "\n",
    "d = 440*256*71\n",
    "n = (217*256*71) + (101*440*71) + (86*440*256)\n",
    "\n",
    "print(d)\n",
    "print(n)\n",
    "print(math.gcd(d,n))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "saisir le rayon : 2\n",
      "saisir la hauteur : 3\n",
      "12.56636\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "\n",
    "pi=3.14159\n",
    "r=int(input(\"saisir le rayon : \"))\n",
    "h=int(input(\"saisir la hauteur : \"))\n",
    "v=(1/3)*pi*r**2*h\n",
    "\n",
    "print(v)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

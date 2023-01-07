{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "720eb20a",
   "metadata": {},
   "source": [
    "# iteration "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "67bd5ddc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3 4 5 6]\n",
      "1 2 3 4 5 6 "
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "arr = np.array([1,2,3,4,5,6])\n",
    "print(arr)\n",
    "\n",
    "for i in arr: \n",
    "    print(i,end=' ')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "cc46dcf2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[12  3  4  5]\n",
      " [12 34 56 78]]\n",
      "12 3 4 5 \n",
      "12 34 56 78 \n"
     ]
    }
   ],
   "source": [
    "array_2d = np.array([[12,3,4,5],[12,34,56,78]])\n",
    "\n",
    "print(array_2d)\n",
    "\n",
    "for i in array_2d:\n",
    "    for j in i:\n",
    "        print(j, end=' ')\n",
    "    print(end='\\n')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2298bc84",
   "metadata": {},
   "source": [
    "# nditer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "7fe61cf7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[[ 1  2  3  4]\n",
      "  [17 34  2  4]\n",
      "  [ 1  2 45 32]]]\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "17\n",
      "34\n",
      "2\n",
      "4\n",
      "1\n",
      "2\n",
      "45\n",
      "32\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "arr = np.array([[[1,2,3,4],[17,34,2,4,],[1,2,45,32]]])\n",
    "\n",
    "print(arr)\n",
    "\n",
    "for d in np.nditer(arr):\n",
    "    print(d)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cf351f48",
   "metadata": {},
   "source": [
    "# ndenumerate"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "41057b5e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[[ 1  2  3  4]\n",
      "  [17 34  2  4]\n",
      "  [ 1  2 45 32]]]\n",
      "(0, 0, 0) 1\n",
      "(0, 0, 1) 2\n",
      "(0, 0, 2) 3\n",
      "(0, 0, 3) 4\n",
      "(0, 1, 0) 17\n",
      "(0, 1, 1) 34\n",
      "(0, 1, 2) 2\n",
      "(0, 1, 3) 4\n",
      "(0, 2, 0) 1\n",
      "(0, 2, 1) 2\n",
      "(0, 2, 2) 45\n",
      "(0, 2, 3) 32\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "arr = np.array([[[1,2,3,4],[17,34,2,4,],[1,2,45,32]]])\n",
    "\n",
    "print(arr)\n",
    "\n",
    "for i,d in np.ndenumerate(arr):\n",
    "    print(i,d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "424774f6",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

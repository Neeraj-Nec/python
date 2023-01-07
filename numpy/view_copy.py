{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "7023a23c",
   "metadata": {},
   "source": [
    "# view vs copy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "7615e4c9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 1 10  3  4  5]\n",
      "[ 1 10  3  4  5]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "arr = np.array([1,2,3,4,5])\n",
    "\n",
    "new = arr.view()\n",
    "arr[1] = 10\n",
    "print(new)\n",
    "print(arr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b7aa7c77",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3 4 5]\n",
      "[ 1 10  3  4  5]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "arr = np.array([1,2,3,4,5])\n",
    "\n",
    "new = arr.copy()\n",
    "arr[1] = 10\n",
    "print(new)\n",
    "print(arr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d8c86bed",
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

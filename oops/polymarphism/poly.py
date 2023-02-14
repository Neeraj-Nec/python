{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "03091552",
   "metadata": {},
   "outputs": [],
   "source": [
    "def test(a, b):\n",
    "    return a + b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "bbb7985f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test(3,4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "7c899f2b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'HelloNeeraj'"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test(\"Hello\", \"Neeraj\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "e9637837",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 3, 4, 6, 7, 8, 9]"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test([1,2,3,4], [6,7,8,9])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "e7419bee",
   "metadata": {},
   "outputs": [],
   "source": [
    "class WebDev:\n",
    "    def syllbas(self):\n",
    "        print(\"This is webDev\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "91b3644d",
   "metadata": {},
   "outputs": [],
   "source": [
    "class DataScience:\n",
    "    def syllbas(self):\n",
    "        print(\"This is datascience\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "b1afa477",
   "metadata": {},
   "outputs": [],
   "source": [
    "def parser(obj):\n",
    "    for obj in obj :\n",
    "        obj.syllbas()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "49312bcb",
   "metadata": {},
   "outputs": [],
   "source": [
    "obj_webDev = WebDev()\n",
    "obj_DataScience = DataScience()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "84843cdd",
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

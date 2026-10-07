{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "308ea633-04cf-4adf-8fcc-0fe2060c5364",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  flight  weather_bad  delay_min\n",
      "0  EK123            0          5\n",
      "1  EK124            1         45\n",
      "2  EK125            0         10\n",
      "3  EK126            1         60\n",
      "4  EK127            0          8\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "import numpy as np\n",
    "\n",
    "data={\n",
    "    'flight':['EK123','EK124','EK125','EK126','EK127'],\n",
    "    'weather_bad':[0,1,0,1,0],     \n",
    "    'delay_min':[5,45,10,60,8]\n",
    "    \n",
    "}\n",
    "df=pd.DataFrame(data)\n",
    "print(df)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "f5b4ca28-595f-4607-8d39-f855efea6ba9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "EK123 > ON TIME\n",
      "EK124 > ITACHELEWA\n",
      "EK125 > ON TIME\n",
      "EK126 > ITACHELEWA\n",
      "EK127 > ON TIME\n"
     ]
    }
   ],
   "source": [
    "def tabiri_delay(weather):\n",
    "    if weather==1:\n",
    "        return \"ITACHELEWA\"\n",
    "    else:\n",
    "        return \"ON TIME\"\n",
    "\n",
    "for i in range(len(df)):\n",
    "    print(f\"{df['flight'][i]} > {tabiri_delay(df['weather_bad'][i])}\")\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "c5bb4f9c-37ce-4aca-a058-3fcd26a7752a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "EK123 >ON TIME\n",
      "EK124 >ITACHELEWA\n",
      "EK125 >ON TIME\n",
      "EK126 >ITACHELEWA\n",
      "EK127 >ON TIME\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "df['status']=np.where(df['weather_bad']==1, 'ITACHELEWA','ON TIME')\n",
    "\n",
    "for flight,status in zip(df['flight'],df['status']):\n",
    "    print(f\"{flight} >{status}\")\n",
    "                      "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "221ce0b1-4356-4bf7-a24a-bdf7bfe0f187",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  flight  weather_bad  delay_min     category\n",
      "0  EK123            0          5      ON TIME\n",
      "1  EK124            1         45  DELAY KUBWA\n",
      "2  EK125            0         10      ON TIME\n",
      "3  EK126            1         60  DELAY KUBWA\n",
      "4  EK127            0          8      ON TIME\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "conditions=[\n",
    "    df['delay_min']<=15,\n",
    "   ( df['delay_min']>15) &(df['delay_min'] <=40),\n",
    "    df['delay_min']>40\n",
    "]\n",
    "choices = ['ON TIME', 'DELAY KIDOGO', 'DELAY KUBWA']\n",
    "df['category'] = np.select(conditions,choices, default='HAIJULIKANI')\n",
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "ecb56535-814b-46e4-8107-b0fde6270103",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Idadi ya Ndege Yenye DELAY KUBWA:2\n",
      "Jumla ya dakika zilizo potea: 105 min\n"
     ]
    }
   ],
   "source": [
    "kubwa=df[df['category']== 'DELAY KUBWA']\n",
    "print(f\"Idadi ya Ndege Yenye DELAY KUBWA:{len(kubwa)}\")\n",
    "print(f\"Jumla ya dakika zilizo potea: {kubwa['delay_min'].sum()} min\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "511145bd-ba2b-44eb-a9b7-f1087d7bd879",
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
   "version": "3.14.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

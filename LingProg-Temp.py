import dht

=import machine

   d = dht.DHT11(machine.Pin(4))


import dht

=import machine

=    d = dht.DHT22(machine.Pin(4))


         d.measure()

         d.temperature()

     d.humidity()
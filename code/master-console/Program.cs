using System.Data;
using System.Diagnostics;
using System.IO.Ports;
using System.Runtime.InteropServices;
using System.Text;

Console.WriteLine("APP Test de comunicacion RS485 to KWC Slaves\n");
while (true)
{
    //Console.Clear();

    // Display available COM ports
    string[] ports = SerialPort.GetPortNames();
    if (ports.Length == 0)
    {
        Console.WriteLine("No hay puertos COM disponibles en el sistema.");
        break;
    }

    Console.WriteLine("Puertos COM disponibles:");
    foreach (var p in ports)
    {
        Console.WriteLine($"  - {p}");
    }
    Console.WriteLine();

    Console.Write("Ingresa el puerto COM asignado al rs485: ");

    string? port = Console.ReadLine();

    if (string.IsNullOrEmpty(port))
    {
        Console.WriteLine("Debe ingresar una opcion...");
        break;
    }

    while (true)
    {
        try
        {
            Console.Write("Ingrese comando: ");
            string cmd = Console.ReadLine();

            using var sp = new SerialPort(port, 9600, Parity.None, 8, StopBits.One);
            sp.Open();
            sp.WriteLine(cmd);
            sp.Close();
            Console.WriteLine($"Mensaje enviado exitosamente a {port}\n");
        }
        catch (System.IO.FileNotFoundException ex)
        {
            Console.WriteLine($"Error: El puerto '{port}' no existe o no está disponible.");
            Console.WriteLine($"Detalles: {ex.Message}\n");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error al comunicarse con el puerto: {ex.Message}\n");
        }
    }
}



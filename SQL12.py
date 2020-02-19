sql = "SELECT Name_of_the_metalls, Tensile_strength FROM Workpiece_material where Name_of_the_metalls like 'А%' and Tensile_strength>25 "# выбор строк и параметра
sql2='PRAGMA table_info(Workpiece_material)'
sql3="SELECT * FROM Workpiece_material where Tensile_strength or Yield_strength or Material_density or M_M or B like '%,%'"
sql4="SELECT * FROM Workpiece_material where Material_density='%,%'"
sql5="Update Workpiece_material SET Material_density= %.% where Material_density = '%,%'"
sql6="select* from The_equipments_of_magnetic_pulse_forming"
sql7='''Insert into The_equipments_of_magnetic_pulse_forming values (?,?,?,?,?,?,?);'''
sql8="Delete from The_equipments_of_magnetic_pulse_forming where Equipment_brand =?"
sql9='''Update The_equipments_of_magnetic_pulse_forming set Equipment_brand =?,Max_charge_energy =?,Condenser_capasity =?,Equipment_inductance =?,Shot_circuit_current_frequency =?,FK1 =?,FK2 =? where Equipment_brand =?'''
class TripData:
  def __init__(self, jdata):
    self.attrs = jdata

  def insert(self, conn):
      cursor = conn.cursor()
      cursor.execute(
          '''INSERT INTO trips 
            (route_id,service_id,trip_id,trip_headsign,trip_short_name,direction_id,block_id,shape_id,wheelchair_accessible,bikes_allowed) 
            VALUES('''\
          + str(self.attrs['route_id']) + ',\'' + str(self.attrs['service_id']) + '\',' + str(self.attrs['trip_id']) + ','
          + '\'' +str(self.attrs['trip_headsign'])+ '\',\'' + str(self.attrs['trip_short_name']) + '\',' + str(self.attrs['direction_id']) + ','
          + str(self.attrs['block_id']) + ',' + str(self.attrs['shape_id']) + ',' + str(self.attrs['wheelchair_accessible']) + ','
          + str(self.attrs['bikes_allowed']) +
            ')')
      for apc_raw in self.attrs['apc_raw']:
          apc_raw_sql = '''INSERT INTO apc_raw (
                act_trip_start_time,actual_sequence,apc_date_time,block_id,
                booking_id,booking_num,booking_start_date,bs_id,
                close_date_time,current_route_id, day_type_vs,direction_code_id,dwell_time,ext_trip_id,
                garage_id,headsign_route,import_error,import_trip_error,insert_date_time,max_load,non_rev_distance,non_rev_seconds,
                num_sat,offs,ons,open_date_time,operator_id,position_source,quality_indicator,raw_max_load,raw_off,raw_on,
                rev_distance,rev_seconds,route_id,run_id,sched_time,seg_arr_time,seg_dep_time,start_trip_time,time_id,tp_id,
                transit_date_time,variation,veh_lat,veh_long,vehicle_id
            ) 
            VALUES('''\
          + '\'' + str(apc_raw['act_trip_start_time'])+ '\',\''+ str(apc_raw['actual_sequence']) + '\',' \
          + '\'' + str(apc_raw['apc_date_time'])+ '\',\''+ str(apc_raw['block_id'])+ '\',' \
          + '\'' + str(apc_raw['booking_id'])+ '\',\''+ str(apc_raw['booking_num'])+ '\',' \
          + '\'' + str(apc_raw['booking_start_date'])+ '\',\''+ str(apc_raw['bs_id'])+ '\',' \
          + '\'' + str(apc_raw['close_date_time'])+ '\',\''+ str(apc_raw['current_route_id'])+ '\',' \
          + '\'' + str(apc_raw['day_type_vs'])+ '\',\''+ str(apc_raw['direction_code_id'])+ '\',' \
          + '\'' + str(apc_raw['dwell_time'])+ '\',\''+ str(apc_raw['ext_trip_id'])+ '\',' \
          + '\'' + str(apc_raw['garage_id'])+ '\',\''+ str(apc_raw['headsign_route'])+ '\',' \
          + '\'' + str(apc_raw['import_error'])+ '\',\''+ str(apc_raw['import_trip_error'])+ '\',' \
          + '\'' + str(apc_raw['insert_date_time'])+ '\',\''+ str(apc_raw['max_load'])+ '\',' \
          + '\'' + str(apc_raw['non_rev_distance'])+ '\',\''+ str(apc_raw['non_rev_seconds'])+ '\',' \
          + '\'' + str(apc_raw['num_sat'])+ '\',\''+ str(apc_raw['offs'])+ '\',' \
          + '\'' + str(apc_raw['ons'])+ '\',\''+ str(apc_raw['open_date_time'])+ '\',' \
          + '\'' + str(apc_raw['operator_id'])+ '\',\''+ str(apc_raw['position_source'])+ '\',' \
          + '\'' + str(apc_raw['quality_indicator'])+ '\',\''+ str(apc_raw['raw_max_load'])+ '\',' \
          + '\'' + str(apc_raw['raw_off'])+ '\',\''+ str(apc_raw['raw_on'])+ '\',' \
          + '\'' + str(apc_raw['rev_distance'])+ '\',\''+ str(apc_raw['raw_on'])+ '\',' \
          + '\'' + str(apc_raw['route_id'])+ '\',\''+ str(apc_raw['run_id'])+ '\',' \
          + '\'' + str(apc_raw['sched_time'])+ '\',\''+ str(apc_raw['seg_arr_time'])+ '\',' \
          + '\'' + str(apc_raw['seg_dep_time'])+ '\',\''+ str(apc_raw['start_trip_time'])+ '\',' \
          + '\'' + str(apc_raw['time_id'])+ '\',\''+ str(apc_raw['tp_id'])+ '\',' \
          + '\'' + str(apc_raw['transit_date_time'])+ '\',\''+ str(apc_raw['variation'])+ '\',' \
          + '\'' + str(apc_raw['veh_lat'])+ '\',\''+ str(apc_raw['veh_long'])+ '\',' \
          + '\'' + str(apc_raw['vehicle_id'] )+  '\'' + ')'
          #print('SQL = {}'.format(apc_raw_sql))
          cursor.execute(apc_raw_sql)
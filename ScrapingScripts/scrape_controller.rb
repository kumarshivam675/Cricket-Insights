require 'nokogiri'
require 'open-uri'
class ScrapeController < ApplicationController
  def init
	# Fetch and parse HTML document
	#@doc = Nokogiri::HTML(open('http://www.iplt20.com/stats'))
	@team_array = ['http://www.iplt20.com/teams/delhi-daredevils','http://www.iplt20.com/teams/gujarat-lions','http://www.iplt20.com/teams/kings-xi-punjab','http://www.iplt20.com/teams/kolkata-knight-riders','http://www.iplt20.com/teams/mumbai-indians','http://www.iplt20.com/teams/rising-pune-supergiants','http://www.iplt20.com/teams/royal-challengers-bangalore','http://www.iplt20.com/teams/sunrisers-hyderabad']


	@doc = Nokogiri::HTML(open('http://datacdn.iplt20.com/dynamic/data/core/cricket/2012/ipl2016/squads.js'))
        @content = open('http://datacdn.iplt20.com/dynamic/data/core/cricket/2012/ipl2016/squads.js').read
	 @content.slice! 'onSquads('
	@content.slice! ');'
	@hash = JSON.parse(@content)
	@squads = @hash['squads']
	#stats test----------------------------------
	#@link  = 'http://datacdn.iplt20.com/dynamic/data/core/cricket/careerStats/'+165.to_s+'_careerStats.js'
	#@stats = open(@link).read
	#@stats.slice! 'onPlayerCareerStats('
	#@stats.slice! ');'
	#@pstat = JSON.parse(@stats)
	#@bStats = @pstat['stats'][1]['breakdown'][12]['tournamentId']['name']
	#@count = 0
	#stat test end ------------------------------
	
	@squads.each do |squad|
		squad['players'].each do |player|
			begin
		  	@count =  player['id'].to_i
			@link  = 'http://datacdn.iplt20.com/dynamic/data/core/cricket/careerStats/'+player['id'].to_s+'_careerStats.js'
			@stats = open(@link).read
			@stats.slice! 'onPlayerCareerStats('
			@stats.slice! ');'
			@tempstat = JSON.parse(@stats)
			@hstat = @tempstat['player']
			@bbStats = @tempstat['stats'][1]['breakdown']
			@index = 0
			
				if(false)
					@index = 15

				else
					@bbStats.each do |bbstat|
						if(bbstat['tournamentId']['name'] == 'ipl2016')
							break
						else
							@index = @index + 1
						end	
					end	
				end			
			@battingStats = @tempstat['stats'][1]['breakdown'][@index]['battingStats']
			@bowlingStats = @tempstat['stats'][1]['breakdown'][@index]['bowlingStats']
			Player.create(:id => player['id'].to_i , :current_team => squad['team']['fullName'] , :name => @hstat['fullName'] , :nationality => @hstat['nationality'], :dob => @hstat['dateOfBirth'] )
		   	PlayerStat.create(:player_id => player['id'].to_i , :matches => @battingStats['m'].to_i , :bat_runs => @battingStats['r'], :bat_avg => @battingStats['a'] ,  :bat_strike_rate => @battingStats['sr'], :bowl_balls => @bowlingStats['b'] , :bowl_runs => @bowlingStats['r'] , :wickets => @bowlingStats['w'] , :bbm => @bowlingStats['bbmr'], :bowl_avg => @bowlingStats['a'] , :economy => @bowlingStats['e'] , :bowl_strike_rate => @bowlingStats['sr'], :_100s =>@battingStats['100s'] ,:_50s =>@battingStats['50s'] , :_4s =>@battingStats['4s'] , :_6s => @battingStats['6s'],:_4W =>@bowlingStats['4W'] , :_5W => @bowlingStats['5W'])
			rescue
				Player.create(:id => player['id'].to_i , :current_team => squad['team']['fullName'] , :name => @hstat['fullName'] , :nationality => @hstat['nationality'], :dob => @hstat['dateOfBirth'] )
			end
		end
	end

        #@squad = @doc.search('div[@class = "row team-overview-columns" ] > div > div > div > div > ul > li')
        
	
  end

end


	# Fetch and parse HTML document
	#@doc = Nokogiri::HTML(open('http://www.iplt20.com/stats'))
	#@team_array = ['http://www.iplt20.com/teams/delhi-daredevils','http://www.iplt20.com/teams/gujarat-lions','http://www.iplt20.com/teams/kings-xi-punjab','http://www.iplt20.com/teams/kolkata-knight-riders','http://www.iplt20.com/teams/mumbai-indians','http://www.iplt20.com/teams/rising-pune-supergiants','http://www.iplt20.com/teams/royal-challengers-bangalore','http://www.iplt20.com/teams/sunrisers-hyderabad']
	#@doc = Nokogiri::HTML(open(@team_array[0])).css('ul')

#<% @js = @doc.xpath('//p').to_s%>

#http://datacdn.iplt20.com/dynamic/data/core/cricket/careerStats/9_careerStats.js  #player stats
#http://static2.iplt20.com/players/284/9.png   #player images

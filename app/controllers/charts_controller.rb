class ChartsController < InheritedResources::Base
  before_action :authenticate_user!

  def create
    @chart = current_user.charts.new(chart_params)
    
    if @chart.save
      redirect_to user_profile_path(current_user), notice: 'Chart was successfully created.'
    else
      render :new
    end
  end

  private

    def chart_params
      params.require(:chart).permit(:user_id, :title, :description, :results, :image)
    end

end

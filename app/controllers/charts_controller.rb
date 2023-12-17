class ChartsController < InheritedResources::Base

  private

    def chart_params
      params.require(:chart).permit(:user_id, :title, :description, :results, :image)
    end

end

class ChartsController < ApplicationController
  before_action :authenticate_user!

  def new
    @chart = Chart.new
  end

  def show
    @chart = Chart.find(params[:id])
  end

  def create
    @chart = current_user.charts.new(chart_params)

    if @chart.save
      process_image_with_openai(@chart)
      redirect_to @chart, notice: 'Chart was successfully created.'
    else
      render :new
    end
  end

  private

  def chart_params
    params.require(:chart).permit(:title, :description, :result, :image)
  end

  def process_image_with_openai(chart)
    if chart.image.attached?
      downloaded_image = chart.image.download
      temp_image_path = Rails.root.join('tmp', chart.image.filename.to_s)
      File.open(temp_image_path, 'wb') { |file| file.write(downloaded_image) }
  
      # Call the Python script with the path of the saved image
      result = `python ./openai_process.py '#{temp_image_path}'`.strip

      # Remove the word 'None' if it is at the end of the string
      result = result.sub(/\s*None\z/, '')

      # Use simple_format to add basic HTML tags (p, br) for line breaks
      formatted_result = helpers.simple_format(result)
  
      chart.update(result: formatted_result)
      File.delete(temp_image_path) if File.exist?(temp_image_path)
    end
  end
  
end

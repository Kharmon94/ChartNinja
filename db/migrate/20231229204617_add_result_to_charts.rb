class AddResultToCharts < ActiveRecord::Migration[7.1]
  def change
    add_column :charts, :result, :text
  end
end

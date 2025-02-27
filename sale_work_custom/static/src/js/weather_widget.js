/** @odoo-module **/
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { Component } from "@odoo/owl";

const actionRegistry = registry.category("actions");

export class WeatherDashboard extends Component {
    setup() {
        super.setup();
        this.orm = useService("orm");
        this.weatherData = {};
        this._fetchWeatherData();
    }

    async _fetchWeatherData() {
        try {
            const weatherRecords = await this.orm.call("weather.app","search_read",[],{ fields: ["city", "weather"]})
            this.weatherData = weatherRecords;
            this.render();  // Force UI update
        } catch (error) {
            console.error("Error fetching weather data", error);
        }
    }
    weather_function(){
     const weatherId = event.currentTarget.dataset.id;
     alert(`Weather Card Clicked! ID: ${weatherId}`);
     console.log('done', weatherId);
    }

}

WeatherDashboard.template = "weather_dashboard_template";
actionRegistry.add("weather_dashboard_action", WeatherDashboard);
